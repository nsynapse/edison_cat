from cv2 import *
cam = VideoCapture(0)
s, img = cam.read()
imwrite("capture.jpg", img)