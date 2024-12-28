import pandas as pd
import re

def preprocess_data(input_path, output_path):
    # Read the dataset while skipping bad lines
    try:
        df = pd.read_csv(input_path, on_bad_lines='skip', engine='python')  # Use 'skip' to skip malformed rows
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Drop rows with missing required columns
    df = df.dropna(subset=['name', 'indication'])

    # Create a column for embedding text
    df['embedding_text'] = df.apply(
        lambda row: f"Drug: {row['name']}. Indication: {row['indication']}. Mechanism: {row['mechanism-of-action']}. Targets: {row['targets']}",
        axis=1
    )

    # Save the cleaned dataset
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data(
        input_path='../data/drugbank_clean.csv',
        output_path='../data/cleaned_drug_data.csv'
    )
