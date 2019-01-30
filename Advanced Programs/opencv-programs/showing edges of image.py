# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:41:24 2018

@author: AbdulBasit0044
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    #images dataset path
    path="images-dataset\\"
    #storing image path explicitly for every image
    imgpath1 = path + "lena_color_512.tif"
    img1=cv2.imread(imgpath1,0)
    #img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    
    laplacian = cv2.Laplacian(img1,cv2.CV_64F)
    sobelx = cv2.Sobel(img1,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img1,cv2.CV_64F,0,1,ksize=5)
    edges = cv2.Canny(img1,10,200)
    edgesl = cv2.Canny(img1,150,200)
    edgesx = cv2.Canny(img1,100,220)
    edgesy = cv2.Canny(img1,100,300)
    
    plt.subplot(2,4,1),plt.imshow(img1,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,5),plt.imshow(edges,cmap = 'gray')
    plt.title('Edges'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,6),plt.imshow(edgesl,cmap = 'gray')
    plt.title('Edges-L'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,7),plt.imshow(edgesx,cmap = 'gray')
    plt.title('Edges-x'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,8),plt.imshow(edgesy,cmap = 'gray')
    plt.title('Edges-y'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    cv2.imshow('image',img1)
    cv2.imshow('image-x',sobelx)
    cv2.imshow('image-y',sobely)
    cv2.imshow('image-laplacian',laplacian)
    cv2.imshow('o-edge',edges)
    cv2.imshow('edge-x',edgesx)
    cv2.imshow('edge-y',edgesy)
    cv2.imshow('edge-laplacian',edgesl)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()