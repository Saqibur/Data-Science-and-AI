import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

test_data = np.random.randint(0, 100, (50, 4))
# print(test_data)

# If no names are given, pandas auto names them.
data_frame = pd.DataFrame(data=test_data, columns=['F1', 'F2', 'F3', 'Label'])
# print(data_frame)

X = data_frame[['F1', 'F2', 'F3']]
Y = data_frame['Label']
# print(X)
# print(Y)

# Random state is a seed, just like random seed in numpy
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_train.shape)
