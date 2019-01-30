# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:28:29 2018
FAST algorithm for Feature Detector
@author: AbdulBasit0044
"""

import numpy as np
import cv2
from  matplotlib import pyplot as plt

def main():
    #reading images
    img=cv2.imread("images-dataset//lena_color_512.tif")
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #creating object of fast feature detection
    fast=cv2.FastFeatureDetector_create(threshold=10)
    #detecting features using fast algorithm
    kp=fast.detect(img,None)
    #drawing keypoints on image
    img2=cv2.drawKeypoints(img,kp,None,color=(255,0,0))
    #printing features values and all default params
    print ("Threshold: ", fast.getThreshold())
    print ("nonmaxSuppression: ", fast.getNonmaxSuppression())
    print ("neighborhood: ", fast.getType())
    print ("Total Keypoints with nonmaxSuppression: ", len(kp))
    #showing image
    cv2.imshow("With nonmaxSuppression",img2)
    #creating object with non max suppression
    fast.setNonmaxSuppression(0)
    kp=fast.detect(img,None)
    #drawing
    img3=cv2.drawKeypoints(img,kp,None,color=(255,0,0))
    #showing images
    cv2.imshow("Without nonmaxSuppression",img3)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    
    
if __name__=="__main__":
    main()