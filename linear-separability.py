from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1,2],[2,3],[3,1],[4,3]])
y = np.array([0,0,1,1])


model = svm.SVC(kernel='linear')
model.fit(x,y)

n_data = np.array([[5,2],[2,1]])
pred = model.predict(n_data)
print(pred)


# lets plot decision boundary for this 
w = model.coef_[0] 
b = model.intercept_[0] 
x1 = np.linspace(1, 4) 
y1 = -(w[0] / w[1]) * x1 - b / w[1] 
plt.plot(x1, y1, 'k-') 

# plot data points 
plt.scatter(x[:, 0], x[:, 1], c=y) 
plt.xlabel('Feature 1') 
plt.ylabel('Feature 2') 
plt.show()
print("Exec Success")
