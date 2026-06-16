from qdrant_client import QdrantClient
from src.embeddings import get_embedding
from config import COLLECTION_NAME

client = QdrantClient(host="localhost", port=6333)

# Test embedding
test_query = "test"
embedding = get_embedding(test_query)
print(f"Embedding generated, dimension: {len(embedding)}")

# Try the search method
try:
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=embedding,
        limit=3
    )
    print("search() worked!")
    print(f"Results type: {type(results)}")
    print(f"Results: {results}")
except Exception as e:
    print(f"search() failed: {e}")

# Try query method
try:
    results = client.query(
        collection_name=COLLECTION_NAME,
        query_vector=embedding,
        limit=3
    )
    print("query() worked!")
    print(f"Results type: {type(results)}")
    print(f"Results: {results}")
except Exception as e:
    print(f"query() failed: {e}")
