from sklearn import svm
import numpy as np

X = np.array([[1,2],[2,3],[3,1],[6,5],[7,7],[8,6]])
y = np.array([0,0,0,1,1,1])

model = svm.SVC(kernel='linear')
model.fit(X,y)

print("Prediction:", model.predict([[4,3]]))
