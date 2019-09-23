import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# '%matplotlib inline' can be used in Jupyter to show pictures inline.

x = np.arange(0, 10)
print(x)
y = x ** 2
# plt.plot(x, y)
# plt.show()

# plt.plot(x, y, '*')
# plt.show()

# plt.plot(x, y, 'bo')
# plt.show()

# There are many more character codes.
plt.plot(x, y, 'red')
plt.xlim(0, 4)
plt.ylim(0, 10)
plt.title("This be my graph")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()

# imshow is used to show images, cmap can have many color formats.
fake_image = np.random.randint(0, 255, (500, 500))
print(fake_image)
plt.imshow(fake_image, cmap="RdYlGn")
plt.colorbar()
plt.show()

