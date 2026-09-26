from dotenv import load_dotenv
load_dotenv()
from rag_pipeline import ask_question




def main():


    print("=" * 60)
    print("RAG Assistant")
    print("Type 'exit' to quit")
    print("=" * 60)


    while True:


        question = input("\nYou: ").strip()


        if question.lower() == "exit":
            print("Goodbye!")
            break


        if not question:
            continue


        try:


            result = ask_question(question)


            print("\nAssistant:")
            print(result["answer"])


            print("\nSources:")


            for source in result["sources"]:
                print(
                    f"- {source['source']} "
                    f"(page {source['page']})"
                )


        except Exception as e:


            print(f"\nError: {e}")




if __name__ == "__main__":
    main()
