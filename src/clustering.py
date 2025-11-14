import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

def plot_dendrogram(X_scaled):
    Z = linkage(X_scaled, method='ward')
    plt.figure(figsize=(12, 6))
    plt.title("Dendrogram (Ward)")
    dendrogram(Z, truncate_mode='level', p=5)
    plt.show()

def elbow_method(X_scaled, max_k=12):
    wcss = []
    for k in range(2, max_k):
        km = KMeans(n_clusters=k, random_state=42, n_init='auto')
        km.fit(X_scaled)
        wcss.append(km.inertia_)
    plt.figure(figsize=(8, 5))
    plt.plot(range(2, max_k), wcss, marker='o')
    plt.title("Elbow Method")
    plt.xlabel("k")
    plt.ylabel("WCSS")
    plt.show()

def final_kmeans(X_scaled, n_clusters):
    km = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    return km.fit_predict(X_scaled)
