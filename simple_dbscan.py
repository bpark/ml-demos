# Importing Modules
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import DBSCAN

# Load Dataset
X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=1)

print(X.shape)
print(y)

# Declaring Model
dbscan = DBSCAN(eps=1.2)

# Fitting
result = dbscan.fit(X)

print(result.labels_)

x_ = X[:, 0]
x_1 = X[:, 1]

plt.scatter(x_, x_1, marker='o', c=result.labels_)
plt.show()

labels = result.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
