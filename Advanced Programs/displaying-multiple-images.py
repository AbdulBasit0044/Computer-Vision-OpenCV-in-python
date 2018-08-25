# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:04:31 2018

@author: AbdulBasit0044
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:30:35 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    #specifying path of dataset
    path="images-dataset\\"
    #giving different images names
    imgpath1=path + "lena_color_512.tif"
    imgpath2=path + "4.2.01.tiff"
    #reading images through opencv funtion
    img1=cv2.imread(imgpath1)
    img2=cv2.imread(imgpath2)
    #converting image color scheme because open cv read images in BGR format but
    #we want to show in RGB format
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    #performing arithematic on images
    add=img1+img2
    sub1=img1-img2
    sub2=img2-img1
    mul=img1*img2
    div=img1/img2
    #storing title for images in array
    titles=['Lena','Drop','Add','i1-i2','i2-i1','mul','div']
    images=[img1,img2,add,sub1,sub2,mul,div]
    #loop to read all images in one go
    for i in range(7):
        plt.subplot(1,7,i+1)#(no. of rows,no. of columns,image no.)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])#removing x-scale
        plt.yticks([])#removing y-scale    
        
    plt.show()
    
    #calling main function
if __name__=="__main__":
    main()