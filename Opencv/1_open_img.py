import cv2 as cv

'''
IMREAD_COLOR (1) loads the image in the BGR 8-bit format.
IMREAD_UNCHANGED (-1) loads the image as is (including the alpha channel if present)
IMREAD_GRAYSCALE (0) loads the image as an intensity one
There are a lot more than these
https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html

'''
img = cv.imread(r'C:\Users\varun\Coding\python_practice\Opencv\car.png',1)
print(img[600,600])
img[600,600] = 0

cv.imshow('WINDOW_NAME',img)   # There has to be a window's name
k = cv.waitKey(0)   # Wait to clase the opened image (milisec)
# 0 means wait forever. 
# DO NOT FORGET TO WRITE cv.waitKey(0) or else image is shown for 1 milisec
if k == ord("s"):   # Only if input key == 's' the image will save
    cv.imwrite("same_car.png",img)