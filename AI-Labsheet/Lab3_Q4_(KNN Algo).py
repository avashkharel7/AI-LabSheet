from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Sample dataset
X = np.array([[1,2],[2,3],[3,1],[6,5],[7,7],[8,6]])
y = np.array([0,0,0,1,1,1])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

test = [[4,3]]
print("Prediction:", model.predict(test))
