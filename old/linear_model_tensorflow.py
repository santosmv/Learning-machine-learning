import numpy as np
from tensorflow import keras
#only one layer, only one neuron (units) and only one entry (one x to one y, input_shape=[1])
model = keras.Sequential([keras.layers.Dense(units=10, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1,2,3,4,5,6,7])
#2x + 1:
ys = np.array([3,5,7,9,11,13,15])

model.fit(xs, ys, epochs=80)

print(model.predict([10]))