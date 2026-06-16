from src.vector_store import client
from src.embeddings import get_embedding
from config import COLLECTION_NAME
from src.vector_store import client

print(type(client))
print("search" in dir(client))
print("query_points" in dir(client))

from src.vector_store import client
from src.embeddings import get_embedding
from config import COLLECTION_NAME

def retrieve_context(query):

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=get_embedding(query),
        limit=3
    )

    results = response.points

    return "\n".join(
        point.payload["text"]
        for point in results
    )
