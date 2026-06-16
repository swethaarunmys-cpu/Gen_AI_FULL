You can create a `README.md` like this and put it in the root of your project.

# RAG Pipeline using Ollama + Qdrant

## Overview

This project implements a simple Retrieval-Augmented Generation (RAG) pipeline using:

* Ollama (Local LLM & Embeddings)
* Qdrant (Vector Database)
* Python
* LangChain Components

The system allows users to upload an HR Policy PDF and ask questions about the document using natural language.

---

## Project Architecture

```text
HR Policy PDF
      │
      ▼
 Document Loader
      │
      ▼
 Text Chunking
      │
      ▼
 Generate Embeddings
 (nomic-embed-text)
      │
      ▼
     Qdrant
(Vector Database)
      │
      ▼
 User Question
      │
      ▼
 Query Embedding
      │
      ▼
 Similarity Search
      │
      ▼
 Retrieved Context
      │
      ▼
 Ollama LLM
 (llama3.2)
      │
      ▼
 Final Answer
```

---

## Project Structure

```text
rag_hr_bot/
│
├── data/
│   └── hr_policy.pdf
│
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── llm.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

### Python

Install Python 3.10 or above.

Verify installation:

```bash
python --version
```

---

### Ollama

Install Ollama:

[https://ollama.com](https://ollama.com)

Pull required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

---

### Qdrant

Run Qdrant using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Verify:

```text
http://localhost:6333/dashboard
```

---

## Installation

Clone or download the project.

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Add Document

Place the HR policy PDF inside:

```text
data/hr_policy.pdf
```

Example:

```text
rag_hr_bot/
└── data/
    └── hr_policy.pdf
```

---

## Index the Document

Run:

```bash
python main.py
```

Select:

```text
1. Ingest PDF
```

This process:

1. Loads the PDF
2. Splits text into chunks
3. Generates embeddings
4. Stores vectors in Qdrant

Expected output:

```text
Indexing Complete
```

---

## Chat with Document

Run:

```bash
python main.py
```

Select:

```text
2. Chat
```

Example:

```text
Ask Question:
What is the leave policy?
```

Example Output:

```text
Summary:
Employees are entitled to 12 casual leaves per year.

Details:
According to the HR policy, employees receive 12 casual leaves annually.

Source:
HR Policy Document
```

Exit chat:

```text
exit
```

---

## Prompt Engineering

The project uses a custom RAG prompt:

```text
You are an expert HR policy assistant.

Instructions:
1. Answer only from the provided context.
2. Do not make up information.
3. If information is unavailable, clearly state it.
4. Keep responses professional and concise.
5. Use bullet points where appropriate.
```

This reduces hallucinations and improves answer quality.

---

## Technologies Used

* Python
* Ollama
* Llama 3.2
* Nomic Embed Text
* Qdrant
* LangChain
* PyPDF

---

## Future Improvements

* FastAPI Backend
* Streamlit UI
* Hybrid Search (BM25 + Vector Search)
* Reranking
* Source Citations
* Metadata Filtering
* Multi-PDF Support
* Conversation Memory
* Evaluation Metrics

---

## Sample Questions

```text
What is the leave policy?

How many casual leaves are allowed?

What is the notice period?

What is the work from home policy?

What happens if an employee resigns?
```

---

## Troubleshooting

### QdrantClient has no attribute 'search'

Replace:

```python
client.search(...)
```

with:

```python
client.query_points(...)
```

for newer Qdrant versions.

---

### Collection Not Found

Ensure PDF ingestion has been completed before using chat mode.

Run:

```text
1. Ingest PDF
```

before selecting:

```text
2. Chat
```

---

## Author

RAG Pipeline using Ollama + Qdrant

Built for learning Retrieval-Augmented Generation (RAG) concepts using local LLMs and vector databases.

This README is detailed enough for a GitHub repository, portfolio project, internship submission, or interview demonstration.
