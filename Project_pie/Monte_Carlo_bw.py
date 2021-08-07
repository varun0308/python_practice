"""
Only black and white images possible
Any size

"""

import numpy as np
import cv2
import random


img = cv2.imread(r'C:\Users\varun\Coding\python_practice\Project_pie\star.png',0)
# Image is as a numpy array

# Getting shape of image
h, w = img.shape

print("Max number of random pixel sampling =",h*w)
print("Give number of test cases(<10000) and number of random pixel sampling.")
n, iterations = [int(x) for x in input().split(' ')]

print("---- Ok wait ----")
# Gets the black pixel ratio for the n test cases 
iteration_list = []

# Makes sure no repeatation of pixel co=ordinates(in the inner samples)
check_list = []

# Count of black and white pixel in the random sampling
count_white = 0
count_black = 0

# n test cases
for _ in range(n) :
    
    # Getting "iteration" number of pixels
    for i in range(iterations):
        # Random pixel values
        x = random.randint(0,h-1)
        y = random.randint(0,w-1)

        # Ensuring no repeatation of pixels
        if [x,y] not in check_list : 
            if img[x,y] == 0 :
                count_black += 1
            else :
                count_white += 1

        else :
            i -= 1

    # Appending black pixel to total value to the list
    ratio_black = float("{:.5f}".format(count_black/(count_black+count_white)))
    iteration_list.append(ratio_black)
    
# Final calculations
mean_ratio_black = sum(iteration_list)/n
print("Percentage of black : %0.5f"%(mean_ratio_black*100))
print("Total black pixel : %d/%d"%(mean_ratio_black*(h*w),(h*w)))