import streamlit as st
from src.ingestion import load_pdf
from src.chunking import create_chunks
from src.vector_store import create_collection,store_chunks
from src.retriever import retrieve_context
from src.llm import generate_answer

st.set_page_config(page_title="HR Policy RAG Chatbot")
st.title("📄 HR Policy RAG Chatbot")

uploaded_file=st.file_uploader("Upload HR Policy PDF",type=["pdf"])

if uploaded_file:
    if st.button("Ingest Document"):
        with open("data/hr_policy.pdf","wb") as f:
            f.write(uploaded_file.read())

        docs=load_pdf("data/hr_policy.pdf")
        chunks=create_chunks(docs)

        create_collection()
        store_chunks(chunks)

        st.success("Document indexed successfully!")

st.divider()

question=st.text_input("Ask a question about the HR Policy")

if st.button("Ask"):
    if question:
        context=retrieve_context(question)
        print("="*50)
        print(context)
        print("="*50)
        answer=generate_answer(question,context)
        st.write("### Answer")
        st.write(answer)
