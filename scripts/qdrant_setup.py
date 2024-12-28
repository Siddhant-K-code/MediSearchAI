from qdrant_client import QdrantClient, models
import json

def upload_to_qdrant(input_path, collection_name):
    client = QdrantClient(url="http://localhost:6333")

    # Load the data
    with open(input_path, 'r') as f:
        data = [json.loads(line) for line in f]

    # Create collection
    vector_size = len(data[0]['embedding'])
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE, on_disk=True)
    )

    # Upload data
    for i, item in enumerate(data):
        client.upsert(
            collection_name=collection_name,
            points=[
                models.PointStruct(
                    id=i,
                    vector=item['embedding'],
                    payload={
                        'name': item['name'],
                        'indication': item['indication'],
                        'mechanism-of-action': item['mechanism-of-action'],
                        'targets': item['targets']
                    }
                )
            ]
        )

if __name__ == "__main__":
    upload_to_qdrant(
        input_path='../data/embedded_drug_data.json',
        collection_name='drug_search'
    )
