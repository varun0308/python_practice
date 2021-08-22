import numpy as np
from PIL import Image
import cv2 


# arr[h,w]
h = 500
w = 1000

arr = np.ones((h, w, 3), dtype='uint8') * 255
print(arr.shape)
# arr[:150,:150, 0] = 150
# arr[350:,:150, 1] = 100
# arr[:150,850:, 1] = 50
# arr[350:,850:, 0] = 0
# arr[150:350,200:800, :2] = 175
arr[:,:,1:] = 0
arr[:,:,0] = 255
image = Image.fromarray(arr)
image.save('test_c_01.png')


# If we use cv2 we do this (replacing last line) : 
# cv2.imwrite(file_name, img) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows()