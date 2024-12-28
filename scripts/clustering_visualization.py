import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
import os

# Create directory for saving charts
os.makedirs("../charts", exist_ok=True)

def plot_clusters():
    # Load embedding data (replace with your actual dataset)
    data = pd.read_json('../data/embedded_drug_data.json', lines=True)
    embeddings = np.array(data['embedding'].tolist())  # Extract embeddings
    labels = data['name']  # Extract drug names for labeling

    # Reduce dimensions using t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    reduced_embeddings = tsne.fit_transform(embeddings)

    # Plot the clusters
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c='blue', alpha=0.5)
    for i, label in enumerate(labels[:50]):  # Annotate a few points
        plt.annotate(label, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]), fontsize=8, alpha=0.7)

    plt.title('t-SNE Visualization of Drug Embeddings')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.savefig("../charts/embedding_clusters.png")
    plt.close()

if __name__ == "__main__":
    plot_clusters()
    print("Clustering chart saved to ../charts/embedding_clusters.png")
