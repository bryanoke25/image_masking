import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)
time.sleep(1)
background = 0

for i in range(60):
    ret, background = video.read()
    if ret == False:
        continue

background = np.flip(background, axis = 1)

while True:
    status,frame = video.read()
    if status == False:
        

