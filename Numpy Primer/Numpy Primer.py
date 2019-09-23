import numpy as np

# Introduction.

test_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# arange not to be confused with "Arrange"
numpy_array = np.arange(15)

print(type(test_array)) # test_array is a list.
print(test_array)

print(type(numpy_array))
print(numpy_array) # The default array type in numpy is ndarray.

zero_array = np.zeros((3, 4))
print(zero_array)
# print(np.ones(100))

# Provides a list of evenly spaced numbers from the start to end.
print(np.linspace(0, 1000, 20))

# arange takes a start, stop, and the distance between the points.
# linspace takes a start, stop, and how many points you want.

print(np.random.randint(0, 100))
print(np.random.randint(0, 100, (3, 3)))


print(np.random.normal(1000))

# Random seeds are important for duplicity
# np.random.seed(101)
print(np.random.randint(0, 100, 10))
# Seeds are reset once a random is generated.

example_array = np.random.randint(0, 100, 10)
print(example_array)
print(example_array.min())
print(example_array.max())
print(example_array.mean())

# For the index location of the max value.
print(example_array.argmax())

# For the index location of the min value.
print(example_array.argmin())

# As long as all values fit, you can reshape to anything.
print(example_array.reshape(2, 5))

# You can use reshape with other distributions.
matrix = np.arange(0, 100, 1).reshape(10, 10)
print(matrix)

# To get a particular item from the 2D matrix.
print(matrix[4][9])

# You can slice as well, using normal python syntax.
# ":" indicates everything.
print(matrix[:, 0])

# Slicing all the way to but not including.
print(matrix[0:2, 0:4])

# Masking a matrix is possible as well.
print (matrix > 50)
print(matrix[matrix > 50])

# NumPy is generally used for array/tensor manipulation.