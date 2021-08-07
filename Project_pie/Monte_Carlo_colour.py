import numpy as np
import cv2
import random


img = cv2.imread(r'C:\Users\varun\Coding\python_practice\Project_pie\template.png',1)
# Image is as a numpy array

# Image has to be grayscale for cv2.threshold()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img_modified = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) 
cv2.imshow('hello',img_modified)

# Getting shape of image
h, w = img.shape

print("Max number of random pixel sampling =",h*w)
print("Give number of test cases(<10000) and number of random pixel sampling.")
n, iterations = [int(x) for x in input().split(' ')]

print("---- Ok wait ----")
# Gets the black pixel ratio for the 100 test cases 
iteration_list = []

# Keeps track of different colours
colour_list = {}

# Makes sure no repeatation of pixel co=ordinates(in the inner samples)
check_list = []

# Count of black and white pixel in the random sampling

# # 100 test cases
# for _ in range(n) :
    
#     # Getting "iteration" number of pixels
#     for i in range(iterations):
#         # Random pixel values
#         x = random.randint(0,h-1)
#         y = random.randint(0,w-1)

#         # Ensuring no repeatation of pixels
#         if [x,y] not in check_list : 
#             if img[x,y] == 0 :
                
#             else :
                

#         else :
#             i -= 1

#     # Appending black pixel to total value to the list
#     ratio_black = float("{:.5f}".format(count_black/(count_black+count_white)))
#     iteration_list.append(ratio_black)
    
# # Final calculations
# mean_ratio_black = sum(iteration_list)/n
# print("Percentage of black : %0.5f"%(mean_ratio_black*100))
# print("Total black pixel : %d/%d"%(mean_ratio_black*(h*w),(h*w)))