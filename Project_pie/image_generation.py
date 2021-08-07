import numpy as np
from PIL import Image
import cv2 


# arr[h,w]
h = 500
w = 1000
"""
^
|
|
|
h

w ------->
"""
arr = np.ones((h, w), dtype='uint8') * 255

arr[:150,:150] = arr[350:,:150] = arr[:150,850:] = arr[350:,850:] = 0
arr[150:350,200:800] = 0

image = Image.fromarray(arr, 'L')
image.save('template.png')


# If we use cv2 we do this : 
# cv2.imwrite(file_name, img) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows()