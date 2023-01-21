from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

X, y = load_boston(return_X_y=True)

from sklearn.neighbors import KNeighborsRegressor

mod = KNeighborsRegressor()

mod.fit(X,y)

pred = mod.predict(X)

plt.scatter(pred, y)
plt.show()