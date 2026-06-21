# Deploying HR Policy RAG Chatbot on GCP Cloud Run

## Prerequisites

- Google Cloud Project
- Billing Enabled
- Cloud Run API Enabled
- Cloud Build API Enabled
- Artifact Registry API Enabled
- OpenAI API Key
- Qdrant Cloud URL and API Key

---

## Project Structure

```text
rag_openai_streamlit/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
│
└── src/
    ├── config.py
    ├── ingestion.py
    ├── chunking.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retriever.py
    └── llm.py
```

---

## Enable Required APIs

```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

---

## Configure Project

```bash
gcloud config set project PROJECT_ID
```

Verify:

```bash
gcloud config get-value project
```

---

## Dockerfile

Create a Dockerfile in the project root.

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["streamlit","run","app.py","--server.port=8080","--server.address=0.0.0.0"]
```

---

## Deploy to Cloud Run

From the project root:

```bash
gcloud run deploy hr-policy-rag \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated
```

Cloud Build will:

1. Build Docker Image
2. Push Image to Artifact Registry
3. Deploy Service to Cloud Run

---

## Configure Environment Variables

After deployment, add the following variables in Cloud Run:

| Variable | Description |
|-----------|------------|
| OPENAI_API_KEY | OpenAI API Key |
| QDRANT_URL | Qdrant Cloud Endpoint |
| QDRANT_API_KEY | Qdrant Cloud API Key |

Using CLI:

```bash
gcloud run services update hr-policy-rag \
  --region asia-south1 \
  --set-env-vars OPENAI_API_KEY=YOUR_KEY,QDRANT_URL=YOUR_URL,QDRANT_API_KEY=YOUR_QDRANT_KEY
```

---

## Access Application

After successful deployment:

```text
https://hr-policy-rag-xxxxx.a.run.app
```

Open the URL in your browser and start using the chatbot.

---

## Architecture

User
→ Streamlit UI (Cloud Run)
→ OpenAI Embeddings
→ Qdrant Cloud Vector Database
→ GPT-4o-mini
→ Response

---

## Features

- PDF Upload
- Document Chunking
- OpenAI Embeddings
- Qdrant Vector Search
- Retrieval Augmented Generation (RAG)
- Streamlit UI
- Cloud Run Deployment