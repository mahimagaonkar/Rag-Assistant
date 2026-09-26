from langchain_groq import ChatGroq


from config import GROQ_API_KEY, GROQ_MODEL




def get_groq_model():


    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not configured")


    if not GROQ_MODEL:
        raise ValueError("GROQ_MODEL is not configured")


    return ChatGroq(
        api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0,
    )
