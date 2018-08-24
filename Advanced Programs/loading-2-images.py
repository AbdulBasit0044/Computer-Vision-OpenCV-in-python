# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:30:35 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    path="images-dataset\\"
    
    imgpath1=path + "lena_color_256.tif"
    imgpath2=path + "4.2.01.tiff"
    
    img1=cv2.imread(imgpath1)
    img2=cv2.imread(imgpath2)
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    plt.subplot(1,2,1)
    plt.imshow(img1)
    plt.title("Lena")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title("Drop")
    plt.xticks([])
    plt.yticks([])
    plt.show()
if __name__=="__main__":
    main()