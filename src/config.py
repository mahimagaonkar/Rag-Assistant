import os
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")


GROQ_MODEL = os.getenv("GROQ_MODEL")
HF_MODEL = os.getenv("HF_MODEL")


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
