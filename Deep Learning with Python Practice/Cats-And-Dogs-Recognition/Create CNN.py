import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

X = pickle.load(open("X-Cat-Dog-Features.pickle", "rb"))
y = pickle.load(open("y-Cat-Dog-Labels.pickle", "rb"))

X = X/255.0

model = Sequential()

#Layer 1
model.add(Conv2D(64, (3, 3), input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

# Layer 2
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

# Layer 3
model.add(Flatten())
model.add(Dense(64))

# Layer 4
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",
            optimizer="adam",
            metrics=['accuracy'])

model.fit(X, y, batch_size=32, epochs=10, validation_split=0.1)