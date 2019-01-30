# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:10:14 2018

Adaptive thresholding

@author: AbdulBasit0044
"""
import cv2
import matplotlib.pyplot as plt

def main():
    
    path="images-dataset\\"
    imgpath=path+"5.1.12.tiff"
    img=cv2.imread(imgpath,0)
    
    block_size=513
    constant=2
    
    th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,constant)
    th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block_size,constant)
    
    titles=["Original","Adaptive Mean","Adaptive Gaussian"]
    images=[img,th1,th2]
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(images[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
if __name__=="__main__":
    main()