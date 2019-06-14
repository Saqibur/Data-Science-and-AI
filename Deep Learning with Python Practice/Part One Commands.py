import tensorflow as tf
import matplotlib.pyplot as plt

print(tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# If we normalize the data we can make the pixel values between 1 and 0.
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

# Try later on without normalizing the data, apparently, it makes a significant difference.

# for i in range(0, 100):
plt.imshow(x_train[0], cmap = plt.cm.binary) # for black and white drawing
# plt.imshow(x_train[i])
plt.show();

# print(x_train[0])