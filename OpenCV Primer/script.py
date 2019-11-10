import cv2

image_path = "./images/penguin.jpg"

image = cv2.imread(image_path)
print(type(image))
print(image)

print(image.ndim)
print(image.shape)

cv2.imshow("Penguin", image)
cv2.waitKey(0)

image = cv2.imread(image_path, 0)
print(image.ndim)
print(image.shape)

cv2.imshow("Grayscale Penguin", image)
cv2.waitKey(0)

resized_image = cv2.resize(image, (600, 600))
cv2.imshow("Resized Penguin", resized_image)
cv2.waitKey(0)

cv2.destroyAllWindows()