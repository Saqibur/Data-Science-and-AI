import cv2, time
from PIL import ImageGrab
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'mp4v') #you can use other codecs as well.
vid = cv2.VideoWriter('record.mp4', fourcc, 8, (500,490))
while(True):
    img = ImageGrab.grab(bbox=(250, 150, 1100, 600)) #x, y, w, h
    img_np = np.array(img)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    vid.write(img_np)
    cv2.imshow("frame", img_np)
    key = cv2.waitKey(1)
    if key == 27:
        break    

vid.release()
cv2.destroyAllWindows()

# camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
camera = cv2.VideoCapture("record.mp4")
face_cascade = cv2.CascadeClassifier()
face_cascade.load('haarcascade_frontalface_default.xml')

fps = 0
while True:
    fps = fps + 1
    check, frame = camera.read()
    # print(check)
    # print(frame)
    # print(type(frame))

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

    for x, y, width, height in faces:
        print("---Face detected---")
        print("X coordinate: ", x)
        print("Y coordinate: ", y)
        print("Width of face: ", width)
        print("Length of face: ", height)
        frame = cv2.rectangle(frame, pt1=(x, y), pt2=(x + width, y + height), color=(0, 255, 0), thickness=2)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        break

print("fps = ", fps)
camera.release()
cv2.destroyAllWindows()
