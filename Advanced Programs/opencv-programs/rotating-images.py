# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:37:54 2018

@author: AbdulBasit0044
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:45:26 2018

Shifting and translating images

@author: AbdulBasit0044
"""

import cv2
import matplotlib.pyplot as plt

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
    #this R is our rotation matrix and the transformation takes place according to it
    R=cv2.getRotationMatrix2D((columns/2,rows/2),45,0.8)
    #showing that matrix is saved correctly
    print(R)
    #applying function to rotate image
    output=cv2.warpAffine(img1,R,(columns,rows))
    #showing output on console
    plt.imshow(output)
    plt.title('Rotated Image')
    plt.show()
    
if __name__=="__main__":
    main()