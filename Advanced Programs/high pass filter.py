# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:43:51 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def main():
    kernel_3x3 = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
    kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                           [-1, 1, 2, 1, -1],
                           [-1, 2, 4, 2, -1],
                           [-1, 1, 2, 1, -1],
                           [-1, -1, -1, -1, -1]])

    img = cv2.imread("images-dataset\\black-white.jpg", 1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    print(img)
    output1=cv2.filter2D(img,-1,kernel_3x3)
    output2=cv2.filter2D(img,-1,kernel_5x5)
    #k3 = ndimage.convolve(img, kernel_3x3)
    #k5 = ndimage.convolve(img, kernel_5x5)
    blurred = cv2.GaussianBlur(img, (11,11), 0)
    g_hpf = img - blurred
    #resizing figure size in pyplot in console
    plt.figure(figsize=(10,10))
    
    plt.subplot(3,1,1)
    plt.imshow(output1)
    plt.title("3x3")
    plt.subplot(3,1,2)
    plt.imshow(output2)
    plt.title("5x5")
    plt.subplot(3,1,3)
    plt.imshow(g_hpf)
    plt.title("g_hpf")
    
    
if __name__=="__main__":
    main()