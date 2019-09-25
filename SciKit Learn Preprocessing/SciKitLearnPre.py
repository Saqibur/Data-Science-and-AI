import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = np.random.randint(0, 100, (10, 2))

print(data)

# Before feeding data into the neural network, you need to scale it.

scaler_model = MinMaxScaler()
scaler_model.fit(data)
scaler_model.transform(data)
print(scaler_model.transform(data))

# The MinMaxScaler transforms all values into between 0 and 1, 0 being min, 1 being max.