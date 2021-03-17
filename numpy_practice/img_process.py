import numpy as np
import cv2

img1 = cv2.imread('../download.jpg',1)

file_name ='img.jpg'

for i in range(185):
    img1[:,i:,2] = i

cv2.imwrite(file_name, img1) 
 
cv2.waitKey(0)  
 
cv2.destroyAllWindows()

