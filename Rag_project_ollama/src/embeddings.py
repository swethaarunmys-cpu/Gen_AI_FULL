import ollama
from config import EMBED_MODEL

def get_embedding(text):
    return ollama.embeddings(model=EMBED_MODEL, prompt=text)["embedding"]
