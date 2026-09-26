from llm.groq_client import get_groq_model
from llm.huggingface_client import get_huggingface_model




def generate_answer(prompt):


    try:


        print("Using Groq...")


        model = get_groq_model()


        response = model.invoke(prompt)


        return response.content


    except Exception as groq_error:


        print(f"Groq failed: {groq_error}")
        print("Falling back to Hugging Face...")


        model = get_huggingface_model()


        response = model.invoke(prompt)


        return response.content
