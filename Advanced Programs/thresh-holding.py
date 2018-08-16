# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:12:47 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    #reading images
    path="images-dataset\\"
    imgpath=path+"gray21.512.tiff"
    img=cv2.imread(imgpath,0)
    #printing image pixels
    print(img)
    #applying thresholding function
    ret, thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret, thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret, thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret, thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret, thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    #arrays for loop
    images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
    titles=["Original","Binary","Binary_Inv","Trunc","Tozero","Tozero_Inv"]
    #loop to display images
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    #calling main
if __name__=="__main__":
    main()