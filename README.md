# 🤖 RAG Assistant Pipeline

A fully functional Retrieval-Augmented Generation (RAG) assistant using LangChain, PostgreSQL (pgvector), Groq, and Hugging Face models.

## 📂 Project Structure
* `main.py` - User chat terminal interface.
* `ingest.py` - Script to parse, chunk, and embed source documents.
* `rag_pipeline.py` - System orchestrating context building and prompt handling.
* `Requirements.txt` - Required python environment packages.

## 🛠️ Local Setup Instructions

1. **Clone the project:**
   ```bash
   git clone <your-repository-url>
   cd rag-assistant
   ```

2. **Set up a Python Virtual Environment:**
   ```bash
   python -m venv .venv
   # Activate on Windows:
   .venv\Scripts\Activate.ps1
   # Activate on Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```

4. **Environment Setup:**
   * Duplicate `.env.example` and rename it to `.env`.
   * Add your actual **Groq** and **Hugging Face** API keys.

5. **Run Document Ingestion:**
   ```bash
   python ingest.py
   ```

6. **Start Chatting:**
   ```bash
   python main.py
   ```
