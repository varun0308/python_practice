import cv2
import numpy as np

image = cv2.imread(r'C:\Users\varun\Coding\python_practice\Opencv\car.png',1)
# cv2.Canny(grayscale image,lower,higher)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny_edged = cv2.Canny(gray,30,200) 

cv2.imshow('Original image',image)
cv2.imshow('Canny edged',canny_edged)

cv2.waitKey(0)
cv2.destroyAllWindows()