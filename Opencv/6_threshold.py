import cv2 as cv
import numpy as np

# For cv.threshold, image HAS to be Grayscale
# ret is the threshold value set by us (127.0 in all, for this case)

img = cv.imread('car.png',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    cv.imshow(titles[i],images[i])
    k = cv.waitKey(0)
    if k == ord('q'):
        break


cv.destroyAllWindows()