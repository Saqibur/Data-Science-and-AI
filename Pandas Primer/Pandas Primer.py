import pandas as pd

# Pandas is usually used for reading in files/datasets.

# Loading in a dataset.
data_frame = pd.read_csv("salaries.csv")
print(data_frame)

print("\n")

# Selecting a specific column
print(data_frame[['Salary', 'Name']])

# You can almost always perform standard numpy operations.
print(data_frame['Salary'].max())

# To get most information about the dataframe.
print(data_frame.describe())

# To get a numpy array from dataframe
# as_matrix will be deprecated
numpy_array = data_frame.as_matrix()

# Use .values instead
numpy_array_values = data_frame.values
print(numpy_array)
print(numpy_array_values)

# You even have a plotting function.
data_frame.plot(x='Salary', y='Age', kind='scatter')

# You will still need matplotlib to actually show it.
