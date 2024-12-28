from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

def search_query(query, collection_name):
    # Load the embedding model
    model = SentenceTransformer("intfloat/multilingual-e5-base", device="cuda")
    query_vector = model.encode(query).tolist()

    # Connect to Qdrant
    client = QdrantClient(url="http://localhost:6333")

    # Perform search
    results = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=5
    )

    # Print results
    for result in results:
        print(f"Name: {result.payload['name']}")
        print(f"Indication: {result.payload['indication']}")
        print(f"Mechanism: {result.payload['mechanism-of-action']}")
        print(f"Targets: {result.payload['targets']}")
        print("-" * 50)

if __name__ == "__main__":
    search_query(
        query="Pain relief for headache",
        collection_name="drug_search"
    )
