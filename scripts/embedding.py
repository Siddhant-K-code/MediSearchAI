from sentence_transformers import SentenceTransformer
import pandas as pd

def generate_embeddings(input_path, output_path):
    # Load the dataset
    df = pd.read_csv(input_path)

    # Load the embedding model
    model = SentenceTransformer("intfloat/multilingual-e5-base", device="cuda")

    # Generate embeddings
    df['embedding'] = df['embedding_text'].apply(lambda text: model.encode(text).tolist())

    # Save with embeddings
    df.to_json(output_path, orient='records', lines=True)

if __name__ == "__main__":
    generate_embeddings(
        input_path='../data/cleaned_drug_data.csv',
        output_path='../data/embedded_drug_data.json'
    )
