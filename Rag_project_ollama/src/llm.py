import ollama
from config import LLM_MODEL

def generate_answer(question, context):

    prompt = f"""
You are an expert HR policy assistant.

Instructions:
1. Answer only from the provided context.
2. Do not make up information.
3. If the answer is not available in the context, say:
   "The HR policy does not contain this information."
4. Keep answers concise and professional.
5. Use bullet points when appropriate.

Context:
---------------------
{context}
---------------------

Employee Question:
{question}

HR Assistant Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]