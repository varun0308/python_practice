import cv2
import numpy as np

image1 = cv2.imread(r'C:\Users\varun\Coding\python_practice\Project_pie\test_c_01_tt.png')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)
cv2.imwrite('test_c_01_tt.png', thresh)
print(ret)

cv2.waitKey(0)
cv2.destroyAllWindows()