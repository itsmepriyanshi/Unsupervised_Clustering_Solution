from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def train_kmeans(df, features, n_clusters):
    """Train a KMeans model on the given features."""
    kmodel = KMeans(n_clusters=n_clusters, init='k-means++').fit(df[features])
    return kmodel

def get_wcss(kmodel):
    """Get the Within Cluster Sum of Squares (WCSS) score."""
    return kmodel.inertia_

def evaluate_silhouette(df, features, labels):
    """Evaluate the silhouette score for the given clustering."""
    return silhouette_score(df[features], labels)