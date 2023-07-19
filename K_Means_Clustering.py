import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Generate sample data
X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=0.7, random_state=42)

# Perform data preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the silhouette score
silhouette_scores = []
max_clusters = 10
for k in range(2, max_clusters+1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

optimal_num_clusters = np.argmax(silhouette_scores) + 2

# Create a K-means clustering object with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=42)
labels = kmeans.fit_predict(X_scaled)
centroids = kmeans.cluster_centers_

# Visualize the clustering results
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', c='red', s=200)
plt.title("K-means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Evaluate the clustering results using silhouette score
silhouette_avg = silhouette_score(X_scaled, labels)
print("Optimal number of clusters:", optimal_num_clusters)
print("Silhouette score:", silhouette_avg)