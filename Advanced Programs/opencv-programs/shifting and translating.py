# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:45:26 2018

Shifting and translating images

@author: AbdulBasit0044
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
    
    #images dataset path
    path="images-dataset\\"
    #storing image path explicitly for every image
    imgpath1 = path + "4.2.06.tiff"
    img1=cv2.imread(imgpath1,1)
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    #extracting shape of image(extracting rows,columns and channels numbers), this is color image so 3 parameters is used
    #channels show that if the image is colored or not
    rows,columns,channels=img1.shape
    #this T is our transformation matrix and the transformation takes place according to it
    T=np.float32([[1,0,100],[0,1,50]])
    #showing that matrix is saved correctly
    print(T)
    #applying function to traslate image
    output=cv2.warpAffine(img1,T,(columns,rows))
    #showing output on console
    plt.imshow(output)
    plt.title('Translated Image')
    plt.show()
    
if __name__=="__main__":
    main()