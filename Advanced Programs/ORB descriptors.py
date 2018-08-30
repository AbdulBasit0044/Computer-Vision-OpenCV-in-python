# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:59:43 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    img=cv2.imread("images-dataset//lena_color_512.tif")
    
    orb=cv2.ORB_create()
    
    kp=orb.detect(img,None)
    
    
    kp, des=orb.compute(img,kp)
    
    img2=cv2.drawKeypoints(img, kp, img, color=(0,0,255),flags=0)
    
    
    
    cv2.imshow("Image",img)
    cv2.imshow("Image2",img2)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    
if __name__=="__main__":
    main()