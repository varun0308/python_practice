# Gives specified colour's focused image (intermidiate HSV(Hue Saturation Value) image)

import cv2 as cv
import numpy as np

while(1):
    # Take each frame
    frame = cv.imread(r'C:\Users\varun\Coding\python_practice\Opencv\car.png',1)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of red color in HSV [R, G, B]
    lower_red = np.array([50,20,20])
    upper_red = np.array([200,255,255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_red, upper_red)
    
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    k = cv.waitKey(0)
    if k == ord('q'):
        break

cv.destroyAllWindows()