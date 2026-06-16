from src.ingestion import load_pdf
from src.chunking import create_chunks
from src.vector_store import create_collection, store_chunks
from src.retriever import retrieve_context
from src.llm import generate_answer

PDF_PATH = "data/hr_policy.pdf"

def ingest():
    docs = load_pdf(PDF_PATH)
    chunks = create_chunks(docs)
    create_collection()
    store_chunks(chunks)
    print("Indexing Complete")

def chat():
    while True:
        q = input("\nAsk Question: ")
        if q.lower() == "exit":
            break
        context = retrieve_context(q)
        answer = generate_answer(q, context)
        print("\nAnswer:\n", answer)

if __name__ == "__main__":
    choice = input("1. Ingest PDF\n2. Chat\nSelect: ")
    if choice == "1":
        ingest()
    elif choice == "2":
        chat()
