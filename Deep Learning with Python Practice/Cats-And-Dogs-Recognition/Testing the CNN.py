import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
testing_data = []
img_array = []

image_size = 50
data_directory = "F:\Testing"


def create_testing_data():
    i = 0
    for image in os.listdir(data_directory):
        
        try:
            img_array = cv2.imread(os.path.join(data_directory, image), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (image_size, image_size))
            plt.imshow(img_array, cmap="gray")
            plt.show()
            # Do no preview images without a break statement.
            testing_data.append([new_array, i])
        except Exception as e:
            pass

        i = i + 1

create_testing_data()
# Change the index, i, to some other number to change which is predicted via the model

testing_data = np.random.randint(3, 4, (50, 50, 1))
testing_data = np.expand_dims(testing_data, axis=0)
new_model = tf.keras.models.load_model('Models/cats-and-dogs-cnn.model')
predictions = new_model.predict(testing_data)

print("Dog" if np.argmax(predictions[0]) else "Cat")
plt.imshow(testing_data[0])
plt.show()
