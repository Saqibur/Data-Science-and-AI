import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

data_directory = "F:\Datasets\PetImages"
# Add your own data directory for the images here.
# Make sure the subfolders are named according to their categories.
categories = ["Cat", "Dog"]

training_data = []

image_size = 50


def create_training_data():
    for category in categories:
        path = os.path.join(data_directory, category)
        class_number = categories.index(category)
        # The path to the images of the cats and dogs.
        for image in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, image), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (image_size, image_size))
                # plt.imshow(img_array, cmap="gray")
                # plt.show()
                # Do no preview images without a break statement.
                training_data.append([new_array, class_number])
            except Exception as e:
                pass

create_training_data()
print(len(training_data))

# Shuffle and balance the data.
random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, image_size, image_size, 1)

# Saving the created data.
pickle_out = open("X-Cat-Dog-Features.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y-Cat-Dog-Labels.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

# Reading the created data.
pickle_in = open("y-Cat-Dog-Labels.pickle", "rb")
X = pickle.load(pickle_in)