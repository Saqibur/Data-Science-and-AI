import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

new_model = tf.keras.models.load_model('number_reader.model')
predictions = new_model.predict(x_test)

print(np.argmax(predictions[0]))

plt.imshow(x_test[0])
