import seaborn as sns
import matplotlib.pyplot as plt

def plot_pairplot(df, features):
    """Plot a pairplot for the given features."""
    sns.pairplot(df[features])
    plt.show()

def plot_elbow(clusters, wcss_scores):
    """Plot the Elbow method graph."""
    plt.plot(clusters, wcss_scores)
    plt.xlabel('No. of clusters')
    plt.ylabel('WSS Score')
    plt.title('Elbow Plot')
    plt.show()

def plot_silhouette(clusters, silhouette_scores):
    """Plot the Silhouette method graph."""
    plt.plot(clusters, silhouette_scores)
    plt.xlabel('No. of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Plot')
    plt.show()