from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


# X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
X = np.array(np.random.random((100, 2)))
kmeans = KMeans(n_clusters=2).fit(X)
print('Labels')
print(kmeans.labels_)
result = kmeans.predict([[0, 0], [12, 3]])
print('result')
print(result)
print('clusters')
print(kmeans.cluster_centers_)

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
