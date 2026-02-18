from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,2],[2,3],[3,1],[6,5],[7,7],[8,6]])

model = KMeans(n_clusters=2, random_state=0)
model.fit(X)

print("Cluster Centers:")
print(model.cluster_centers_)

print("Labels:")
print(model.labels_)
