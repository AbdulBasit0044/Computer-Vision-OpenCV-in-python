# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:50:26 2018
Blending and merging two images
@author: AbdulBasit0044
"""
import cv2
import numpy as np

#reading images
img1=cv2.imread("images-dataset\\baseball_ball.png")
img2=cv2.imread("images-dataset\\football_ball.jpg")
#resizing images because iamges are too big
img1=cv2.resize(img1,(500,500))
img2=cv2.resize(img2,(500,500))
#merging images
footbase_ball=np.hstack((img1[:,:250],img2[:,250:]))


# Constructing Gaussian Pyramid 1
layer=img1.copy()# taking copy so that original image cannot be disturbed
# 1 index contains original image
gaussian_pyramid1=[layer]
# creating pyramid by pyrDown()
for i in range(6):
    layer=cv2.pyrDown(layer)
    # appending to the gaussian pyramid
    gaussian_pyramid1.append(layer)

# Laplacian Pyramid 1
layer=gaussian_pyramid1[5]
# 1 index contains smallest gaussian pyramid image
laplacian_pyramid1=[layer]
for i in range(5,0,-1):
    # getting width and height so that when subtraction takes place then there is no error due to different sizes of images
    #here we want to generate the size of the gaussian pyramid so take it as arhument
    size=(gaussian_pyramid1[i-1].shape[1],gaussian_pyramid1[i-1].shape[0])
    #pyrUp and setting size of image to be formed
    gaussian_expanded=cv2.pyrUp(gaussian_pyramid1[i], dstsize=size)
    # calculating laplacian by subtracting
    laplacian=cv2.subtract(gaussian_pyramid1[i-1],gaussian_expanded)
    # expanding laplacian so that index 6 contains laplacian of the original size
    laplacian_pyramid1.append(laplacian)



# Constructing Gaussian Pyramid 2
layer=img2.copy()# taking copy so that original image cannot be disturbed
# 1 index contains original image
gaussian_pyramid2=[layer]
# creating pyramid by pyrDown()
for i in range(6):
    layer=cv2.pyrDown(layer)
    # appending to the gaussian pyramid
    gaussian_pyramid2.append(layer)

# Laplacian Pyramid 2
layer=gaussian_pyramid2[5]
# 1 index contains smallest gaussian pyramid image
laplacian_pyramid2=[layer]
for i in range(5,0,-1):
    # getting width and height so that when subtraction takes place then there is no error due to different sizes of images
    #here we want to generate the size of the gaussian pyramid so take it as arhument
    size=(gaussian_pyramid2[i-1].shape[1],gaussian_pyramid2[i-1].shape[0])
    #pyrUp and setting size of image to be formed
    gaussian_expanded=cv2.pyrUp(gaussian_pyramid2[i], dstsize=size)
    # calculating laplacian by subtracting
    laplacian=cv2.subtract(gaussian_pyramid2[i-1],gaussian_expanded)
    # expanding laplacian so that index 6 contains laplacian of the original size
    laplacian_pyramid2.append(laplacian)
    
    
# Laplacian pyramid Footbase ball
footbase_ball_pyramid=[]
n=0
#excessing two arrays so that merge them in one laplacian
for img1_lap,img2_lap in zip(laplacian_pyramid1,laplacian_pyramid2):
    n+=1
    #for shape calculating rows and columns
    cols,rows,ch=img1_lap.shape
    #merging two arrays together and accessing together
    laplacian=np.hstack((img1_lap[:,0:int(cols/2)],img2_lap[:,int(cols/2):]))
    #appending footbase ball laplacian
    footbase_ball_pyramid.append(laplacian)

#reconstructing image from footbase ball pyramid    
footbase_ball_reconstructed=footbase_ball_pyramid[0]
for i in range(1,6):
    #calculating size and then reconstructing image
    size=(footbase_ball_pyramid[i].shape[1],footbase_ball_pyramid[i].shape[0])
    footbase_ball_reconstructed=cv2.pyrUp(footbase_ball_reconstructed,dstsize=size)
    footbase_ball_reconstructed=cv2.add(footbase_ball_pyramid[i],footbase_ball_reconstructed)

#showing iamge
cv2.imshow("Footbase-ball",footbase_ball_reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()
