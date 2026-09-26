import psycopg2
from pgvector.psycopg2 import register_vector


from config import DATABASE_URL




def store_documents(chunks, embeddings):


    connection = psycopg2.connect(DATABASE_URL)
    register_vector(connection)


    cursor = connection.cursor()


    for chunk in chunks:


        content = chunk.page_content


        source_file = chunk.metadata.get(
            "source_file",
            "Unknown"
        )


        page = chunk.metadata.get(
            "page",
            None
        )


        embedding = embeddings.embed_query(content)


        cursor.execute(
            """
            INSERT INTO document_chunks
            (content, source_file, page, embedding)
            VALUES (%s, %s, %s, %s)
            """,
            (
                content,
                source_file,
                page,
                embedding
            )
        )


    connection.commit()


    cursor.close()
    connection.close()


    print(f"Stored {len(chunks)} chunks in document_chunks")
   

