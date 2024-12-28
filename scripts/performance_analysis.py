import matplotlib.pyplot as plt
import os

# Create directory for saving charts
os.makedirs("../charts", exist_ok=True)

def plot_performance():
    methods = ['MySQL Full-Text', 'Qdrant Vector Search']
    search_time = [0.73, 91]  # in milliseconds
    accuracy = [80, 95]       # in percentage

    # Plot search time
    plt.figure(figsize=(10, 5))
    plt.bar(methods, search_time, color=['blue', 'orange'])
    plt.title('Search Time Comparison')
    plt.ylabel('Time (ms)')
    plt.xlabel('Search Method')
    plt.ylim(0, max(search_time) + 20)
    plt.savefig("../charts/search_time_comparison.png")
    plt.close()

    # Plot accuracy
    plt.figure(figsize=(10, 5))
    plt.bar(methods, accuracy, color=['blue', 'orange'])
    plt.title('Accuracy Comparison')
    plt.ylabel('Accuracy (%)')
    plt.xlabel('Search Method')
    plt.ylim(0, 100)
    plt.savefig("../charts/accuracy_comparison.png")
    plt.close()

if __name__ == "__main__":
    plot_performance()
    print("Performance charts saved to ../charts/")
