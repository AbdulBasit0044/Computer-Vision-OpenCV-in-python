# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 12:16:31 2018

@author: AbdulBasit0044
"""

import cv2

img=cv2.imread("images-dataset\\hand.jpg")

layer=img.copy()

gaussian_pyramid=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    #cv2.imshow(str(i),gaussian_pyramid[i])
    
    
layer=gaussian_pyramid[5]
laplacian_pyramid=[layer]
for i in range(5,0,-1):
    size=(gaussian_pyramid[i-1].shape[1],gaussian_pyramid[i-1].shape[0])
    gaussian_expansion=cv2.pyrUp(gaussian_pyramid[i],dstsize=size)
    laplacian=cv2.subtract(gaussian_pyramid[i-1],gaussian_expansion)
    laplacian_pyramid.append(laplacian)
    #cv2.imshow(str(i),laplacian)   

r_image=laplacian_pyramid[0]
for i in range(1,6):
    size=(laplacian_pyramid[i].shape[1],laplacian_pyramid[i].shape[0])
    gaussian_expansion=cv2.pyrUp(r_image,dstsize=size)
    r_image=cv2.add(gaussian_expansion,laplacian_pyramid[i])
    cv2.imshow(str(i),r_image)

cv2.waitKey()
cv2.destroyAllWindows()