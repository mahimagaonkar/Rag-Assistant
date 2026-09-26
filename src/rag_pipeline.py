from retrieval.retriever import retrieve_documents
from llm.model_manager import generate_answer




SYSTEM_PROMPT = """
You are a helpful RAG assistant.


Answer the user's question using only the provided context.


Rules:
1. Do not make up information.
2. If the answer is not present in the context, say:
   "I could not find the answer in the provided documents."
3. Keep the answer clear and concise.
4. Use the document context as your primary source.
"""




def build_context(documents):
    """
    Convert retrieved LangChain documents into context
    for the LLM.
    """


    context_parts = []


    for i, document in enumerate(documents, start=1):


        source = document.metadata.get(
            "source_file",
            "Unknown"
        )


        page = document.metadata.get(
            "page",
            "Unknown"
        )


        context_parts.append(
            f"""
--- Context {i} ---
Source: {source}
Page: {page}


{document.page_content}
"""
        )


    return "\n".join(context_parts)




def ask_question(question: str, k: int = 5):


    # 1. Retrieve relevant documents
    documents = retrieve_documents(
        question,
        k=k
    )


    # 2. Check whether anything was retrieved
    if not documents:
        return {
            "answer": "I could not find relevant information in the provided documents.",
            "sources": []
        }


    # 3. Build context
    context = build_context(documents)


    # 4. Build prompt
    prompt = f"""
{SYSTEM_PROMPT}


CONTEXT:
{context}


USER QUESTION:
{question}


ANSWER:
"""


    # 5. Send to Groq → HF fallback
    answer = generate_answer(prompt)


    # 6. Collect sources
    sources = []


    for document in documents:


        source = document.metadata.get(
            "source_file",
            "Unknown"
        )


        page = document.metadata.get(
            "page",
            "Unknown"
        )


        sources.append({
            "source": source,
            "page": page
        })


    return {
        "answer": answer,
        "sources": sources
    }


