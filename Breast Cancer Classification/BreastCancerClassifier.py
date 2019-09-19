import pandas as pd
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

X_train = pd.read_csv("F:\\Datasets\\Breast Cancer Classification\\xtrain.csv", header=None)
Y_train = pd.read_csv("F:\\Datasets\\Breast Cancer Classification\\ytrain.csv", header=None)


classifier = Sequential() # Initialising the ANN

classifier.add(Dense(units = 16, activation = 'relu', input_dim = 30))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 6, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy')

classifier.fit(X_train, Y_train, batch_size = 1, epochs = 100)

classifier.save("breast_cancer_classifier.model")