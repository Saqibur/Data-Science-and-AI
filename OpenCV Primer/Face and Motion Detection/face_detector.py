import cv2
import numpy as np

harrcascade_face_path = cv2.data.haarcascades + "harrcascade_frontalface_default.xml"
print(harrcascade_face_path)
face_cascade = cv2.CascadeClassifier()

face_cascade.load('haarcascade_frontalface_default.xml')

print(face_cascade)
print(face_cascade.empty())

image_path = "./images/barca.jpg"

image = cv2.imread(image_path)
resized_image = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))

gray_img =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Before Face Detection", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Smaller scale factor fives higher accuracy.
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# print(faces)

for x, y, width, height in faces:
    print("---Face detected---")
    print("X coordinate: ", x)
    print("Y coordinate: ", y)
    print("Width of face: ", width)
    print("Length of face: ", height)
    image = cv2.rectangle(image, pt1=(x, y), pt2=(x + width, y + height), color=(0, 255, 0), thickness=2)

resized_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
cv2.imshow("After Face Detection", resized_image)
cv2.waitKey(0)

print("Detected ", len(faces), " faces.")