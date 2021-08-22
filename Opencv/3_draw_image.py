import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((500,500,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(120,420),(460,34),(55,100,67),3)
# cv.line(image,initial co,final co, colour,thickness)

cv.rectangle(img,(120,34),(460,420),(0,255,0),3)
# cv.rectangle(image,top-left corner, bottom-right corner,colour,thickness)

cv.circle(img,(147,63), 63, (0,0,255),1)
#               centre, radius   fills colour for -1

pts = np.array([[8,8],[139,45],[344,56],[17,398]],np.int32)
pts = pts.reshape(-1,1,2)
print(pts.shape)
cv.polylines(img,[pts],True,(0,0,255),5)
# If False, it will not be a closed figure

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'This is NOT easy :\'(',(0,480), font,1.5,(255,255,255),2,cv.LINE_AA)

cv.imshow('Hello',img)
cv.waitKey(0)
cv.destroyAllWindows()

