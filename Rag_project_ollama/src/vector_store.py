from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from config import COLLECTION_NAME
from src.embeddings import get_embedding

client = QdrantClient(host="localhost", port=6333)

def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE)
    )

def store_chunks(chunks):
    points = []
    for idx, chunk in enumerate(chunks):
        embedding = get_embedding(chunk.page_content)
        points.append(
            PointStruct(
                id=idx,
                vector=embedding,
                payload={"text": chunk.page_content}
            )
        )
    client.upsert(collection_name=COLLECTION_NAME, points=points)
