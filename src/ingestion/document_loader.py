
from pathlib import Path


from langchain_community.document_loaders import (
    PyPDFLoader,
TextLoader,
)





DOCUMENTS_DIR = Path(__file__).resolve().parent.parent.parent / "data"





def load_documents():
    documents = []


    if not DOCUMENTS_DIR.exists():
        raise FileNotFoundError(
            f"Directory not found: {DOCUMENTS_DIR}"
        )


    files = [
        file for file in DOCUMENTS_DIR.rglob("*")
        if file.is_file()
    ]


    if not files:
        raise FileNotFoundError(
            "No documents found in data/documents/"
        )


    for file_path in files:


        suffix = file_path.suffix.lower()


        try:


            if suffix == ".pdf":
                loader = PyPDFLoader(str(file_path))


            elif suffix == ".txt":
                loader = TextLoader(
                    str(file_path),
                    encoding="utf-8"
                )


            else:
                print(
                    f"Skipping unsupported file: {file_path.name}"
                )
                continue


            print(f"Loading: {file_path}")


            docs = loader.load()


            for doc in docs:
                doc.metadata["source_file"] = file_path.name
                doc.metadata["file_path"] = str(file_path)


            documents.extend(docs)


        except Exception as e:
            print(
                f"Error loading {file_path.name}: {e}"
            )


    print(f"Total documents/pages loaded: {len(documents)}")


    return documents

