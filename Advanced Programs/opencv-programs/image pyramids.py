# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 12:16:19 2018

creating pyramids of image and then reconstructing to
apply blending effect

@author: AbdulBasit0044
"""

import cv2
# Reading image
img=cv2.imread("images-dataset\\hand.jpg")

# Constructing Gaussian Pyramid
layer=img.copy()# taking copy so that original image cannot be disturbed
# 1 index contains original image
gaussian_pyramid=[layer]
# creating pyramid by pyrDown()
for i in range(6):
    layer=cv2.pyrDown(layer)
    # appending to the gaussian pyramid
    gaussian_pyramid.append(layer)

# Laplacian Pyramid
layer=gaussian_pyramid[5]
cv2.imshow("6",layer)
# 1 index contains smallest gaussian pyramid image
laplacian_pyramid=[layer]
for i in range(5,0,-1):
    # getting width and height so that when subtraction takes place then there is no error due to different sizes of images
    #here we want to generate the size of the gaussian pyramid so take it as arhument
    size=(gaussian_pyramid[i-1].shape[1],gaussian_pyramid[i-1].shape[0])
    #pyrUp and setting size of image to be formed
    gaussian_expanded=cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    # calculating laplacian by subtracting
    laplacian=cv2.subtract(gaussian_pyramid[i-1],gaussian_expanded)
    # expanding laplacian so that index 6 contains laplacian of the original size
    laplacian_pyramid.append(laplacian)

#reconstructing and blending image
#index 0 contains the small gaussian pyramid image(last downed image)
reconstructed_image=laplacian_pyramid[0]
for i in range(1,6):
    #caclculating the size for the new image to be reconstructed
    size=(laplacian_pyramid[i].shape[1],laplacian_pyramid[i].shape[0])
    #pyrUp image(first image or reconstruced pyramid)
    reconstructed_image=cv2.pyrUp(reconstructed_image, dstsize=size)
    #adding laplacian so that image can be reconstructed
    #dulled uped + laplacian of same size to reconstruct image
    reconstructed_image=cv2.add(reconstructed_image,laplacian_pyramid[i])
    #displaying images
    cv2.imshow(str(i),reconstructed_image)

#displaying original image
cv2.imshow("Original Imgae",img)
cv2.waitKey(0)
cv2.destroyAllWindows()