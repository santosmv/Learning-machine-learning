import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

#take the dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#creating a model to optimize
model = keras.Sequential([
    #28: number of pixels of each image (entries)
    keras.layers.Flatten(input_shape=(28,28)),
    #128: number of functions to be optimized
    keras.layers.Dense(128, activation=tf.nn.relu),
    #10: number of fashion items
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

#compiling the model
model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy')

#fit the model to data
model.fit(train_images, train_labels, epochs=3)

#results of the evaluation
results = model.evaluate(test_images, test_labels)

predictions = model.predict(test_images)
#print(predictions)

for i in range(len(test_labels)):
    predict_number = np.argmax(predictions[i])
    print('valor verdadeiro =', test_labels[i], 'predição =', predict_number)

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(True)
plt.show()