import psycopg2
from pgvector.psycopg2 import register_vector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from sentence_transformers import CrossEncoder  # For Reranking
from config import DATABASE_URL, EMBEDDING_MODEL

# 1. Load the Embedding Model (unchanged)
def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# 2. Load the Reranker Model (Lightweight, fast model)
def get_reranker():
    return CrossEncoder("mixedbread-ai/mxbai-rerank-xsmall-v1")

def retrieve_documents(question: str, k: int = 5):
    """
    1. Hybrid Search: Combines Vector Search (<=>) and Keyword Search (tsvector)
    2. Reranking: Recalculates relevance and puts the top k results first.
    """
    embeddings = get_embeddings()
    query_embedding = embeddings.embed_query(question)

    connection = psycopg2.connect(DATABASE_URL)
    register_vector(connection)
    cursor = connection.cursor()

    # HYBRID SEARCH QUERY
    # We fetch a larger pool of candidates (e.g., 20) so the reranker has options to re-sort.
    cursor.execute(
        """
        WITH vector_search AS (
            SELECT id, content, source_file, page,
                   (1 - (embedding <=> %s::vector)) AS vector_score
            FROM document_chunks
            ORDER BY embedding <=> %s::vector
            LIMIT 20
        ),
        keyword_search AS (
            SELECT id, content, source_file, page,
                   ts_rank_cd(to_tsvector('english', content), plainto_tsquery('english', %s)) AS keyword_score
            FROM document_chunks
            WHERE to_tsvector('english', content) @@ plainto_tsquery('english', %s)
            LIMIT 20
        )
        SELECT 
            COALESCE(v.content, k.content) as content,
            COALESCE(v.source_file, k.source_file) as source_file,
            COALESCE(v.page, k.page) as page
        FROM vector_search v
        FULL OUTER JOIN keyword_search k ON v.id = k.id
        ORDER BY (COALESCE(v.vector_score, 0) + COALESCE(k.keyword_score, 0)) DESC
        LIMIT 20;
        """,
        (query_embedding, query_embedding, question, question)
    )

    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    if not rows:
        return []

    # Prepare standard LangChain Document structures
    initial_documents = []
    for row in rows:
        initial_documents.append(
            Document(
                page_content=row[0],
                metadata={"source_file": row[1], "page": row[2]}
            )
        )

    # RERANKING PHASE
    reranker = get_reranker()
    
    # Pair the user question with each retrieved document snippet
    pairs = [[question, doc.page_content] for doc in initial_documents]
    
    # Calculate exact relevancy scores
    rerank_scores = reranker.predict(pairs)

    # Attach the scores to the documents and sort them highest-to-lowest
    for idx, score in enumerate(rerank_scores):
        initial_documents[idx].metadata["rerank_score"] = float(score)
        
    initial_documents.sort(key=lambda x: x.metadata["rerank_score"], reverse=True)

    # Return only the top 'k' requested best documents
    return initial_documents[:k]
