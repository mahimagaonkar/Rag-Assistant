from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


from config import HF_API_KEY, HF_MODEL
def get_huggingface_model():


    if not HF_API_KEY:
        raise ValueError("HF_API_KEY is not configured")


    if not HF_MODEL:
        raise ValueError("HF_MODEL is not configured")


    llm = HuggingFaceEndpoint(
        repo_id=HF_MODEL,
        huggingfacehub_api_token=HF_API_KEY,
        temperature=0,
        max_new_tokens=512,
    )


    return ChatHuggingFace(llm=llm)

