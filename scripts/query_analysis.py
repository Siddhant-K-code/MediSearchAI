import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Create directory for saving charts
os.makedirs("../charts", exist_ok=True)

def plot_query_analysis():
    # Sample data (replace with actual query performance metrics)
    query_times = {
        'MySQL Full-Text': np.random.normal(0.73, 0.1, 100),
        'Qdrant Vector Search': np.random.normal(91, 5, 100)
    }

    # Create a DataFrame for visualization
    df = pd.DataFrame({
        'Method': ['MySQL Full-Text'] * 100 + ['Qdrant Vector Search'] * 100,
        'Query Time (ms)': np.concatenate([query_times['MySQL Full-Text'], query_times['Qdrant Vector Search']])
    })

    # Plot a boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Method', y='Query Time (ms)', data=df)
    plt.title('Distribution of Query Response Times')
    plt.savefig("../charts/query_response_times.png")
    plt.close()

if __name__ == "__main__":
    plot_query_analysis()
    print("Query analysis chart saved to ../charts/query_response_times.png")
