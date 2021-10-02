import cv2 as cv
from matplotlib import pyplot as plt

img_bw = cv.imread(r'sudoku.jpg',0)

laplacian = cv.Laplacian(img_bw,cv.CV_64F)

plt.subplot(2,2,1),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian_plt'), plt.xticks([]), plt.yticks([])

cv.imshow('Original',img_bw)
cv.imshow('Laplacian_cv',laplacian)
cv.imwrite('Laplacian_cv.jpg',laplacian)
cv.imwrite('Original.jpg',img_bw)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()