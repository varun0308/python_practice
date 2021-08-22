import cv2 as cv
import numpy as np

image = cv.imread(r'\car.png',1)
light = image[430:560,150:200]

# Replacing a specific part of image with same as light
image[430:560,30:80] = light
cv.imwrite('car_copied.png',image)