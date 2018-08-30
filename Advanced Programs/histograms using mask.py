# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:48:33 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    img=cv2.imread("images-dataset\\hand.jpg",0)
    img=cv2.resize(img,(500,500))
    
    #creating mask
    mask=np.zeros(img.shape[:2],np.uint8)
    mask[100:400,100:400]=255
    masked_img=cv2.bitwise_and(img,img,mask = mask)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Original Image",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    hist_full=cv2.calcHist([img],[0],None,[256],[0,256])    
    hist_mask=cv2.calcHist([img],[0],mask,[256],[0,256])
    
    plt.subplot(4,1,1)
    plt.imshow(img,'gray')
    plt.subplot(4,1,2)
    plt.imshow(mask,'gray')
    plt.subplot(4,1,3)
    plt.imshow(masked_img,'gray')
    plt.subplot(4,1,4)
    plt.plot(hist_full)
    plt.plot(hist_mask)
    
if __name__=="__main__":
    main()