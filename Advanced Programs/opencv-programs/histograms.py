# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:49:46 2018
finding histograms
@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    img=cv2.imread("images-dataset\\4.1.04.tiff",1)
    img=cv2.resize(img,(500,500))
    
    
    #making histogram from numpy function
    histogram=np.histogram(img.ravel(),256,[0,256])
    
    #displaying histogram in matplotlib pyplot
    plt.hist(img.ravel(),256,[0,256])
    plt.title('solid histogram')
    plt.show()
    #array of names of colors as argument
    color=('b','g','r')
    #showing histogram of differengt colors in BGR format
    for i,col in enumerate(color):
        hist=cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist,color=col)
        plt.xlim([0,256])
    plt.show()
    
#    cv2.imshow("Image",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()