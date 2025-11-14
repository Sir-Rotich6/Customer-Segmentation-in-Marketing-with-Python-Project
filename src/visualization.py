import matplotlib.pyplot as plt

def scatter_plot(df, cluster_col):
    plt.figure(figsize=(8,5))
    plt.scatter(df["minutes_watched"], df["CLV"], c=df[cluster_col])
    plt.xlabel("Minutes Watched")
    plt.ylabel("CLV")
    plt.title("Cluster Visualization")
    plt.show()
