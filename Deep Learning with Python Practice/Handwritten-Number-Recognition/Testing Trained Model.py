import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

new_model = tf.keras.models.load_model('Models/number_reader.model')
predictions = new_model.predict(x_test)

# Change the index, i, to some other number to change which is predicted via the model

i = 96

print(np.argmax(predictions[i]))

plt.imshow(x_test[i])
plt.show()
