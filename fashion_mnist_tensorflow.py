import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = keras.Sequential([
    #28: number of pixels of each image
    keras.layers.Flatten(input_shape=(28,28)),
    #128: number of functions to be optimized
    keras.layers.Dense(128, activation=tf.nn.relu),
    #10: nmber of fashion items
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy')

model.fit(train_images, train_labels, epochs=1)

results = model.evaluate(test_images, test_labels)

predictions = model.predict(test_images)
print(predictions[0])

predict_number = np.argmax(predictions[0])
print(predict_number)

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()