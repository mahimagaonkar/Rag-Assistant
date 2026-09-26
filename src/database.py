from langchain_postgres import PGVector


from config import DATABASE_URL




def get_vector_store(embeddings):
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name="rag_documents",
        connection=DATABASE_URL,
        use_jsonb=True,
    )


    return vector_store
