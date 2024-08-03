from src.data_preparation import load_data, describe_data, check_shape
from src.clustering import train_kmeans, get_wcss, evaluate_silhouette
from src.visualization import plot_pairplot, plot_elbow, plot_silhouette

# Load Data
df = load_data('data/mall_customers.csv')

# Data Description and Shape
print(describe_data(df))
print(check_shape(df))

# Feature Selection
features = ['Age', 'Annual_Income', 'Spending_Score']

# Pairplot
plot_pairplot(df, features)

# KMeans Clustering
kmodel = train_kmeans(df, features, n_clusters=5)

# Elbow Method
clusters = range(3, 9)
wcss_scores = [get_wcss(train_kmeans(df, features, n)) for n in clusters]
plot_elbow(clusters, wcss_scores)

# Silhouette Method
silhouette_scores = [evaluate_silhouette(df, features, train_kmeans(df, features, n).labels_) for n in clusters]
plot_silhouette(clusters, silhouette_scores)