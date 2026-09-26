from ingestion.document_loader import load_documents
from ingestion.text_splitter import split_documents
from ingestion.embeddings import get_embeddings
from ingestion.vector_store import store_documents




def main():


    print("1. Loading documents...")
    documents = load_documents()


    print("2. Splitting documents...")
    chunks = split_documents(documents)


    print("3. Loading embedding model...")
    embeddings = get_embeddings()


    print("4. Storing documents in PostgreSQL...")
    store_documents(chunks, embeddings)


    print("\nIngestion completed successfully!")




if __name__ == "__main__":
    main()
from ingestion.document_loader import load_documents
from ingestion.text_splitter import split_documents
from ingestion.embeddings import get_embeddings
from ingestion.vector_store import store_documents




def main():


    print("1. Loading documents...")
    documents = load_documents()


    print("2. Splitting documents...")
    chunks = split_documents(documents)


    print("3. Loading embedding model...")
    embeddings = get_embeddings()


    print("4. Storing documents in PostgreSQL...")
    store_documents(chunks, embeddings)


    print("\nIngestion completed successfully!")




if __name__ == "__main__":
    main()
