# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:41:41 2018
Finding attributes or Harris corner detection
@author: AbdulBasit0044
"""

import cv2
import numpy as np

def main():
    
    img=cv2.imread("images-dataset\\chess board.jpg")
    img=cv2.resize(img,(2000,2000))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #making numpy array
    gray=np.float32(gray)
    #applying harris corner detection
    dst=cv2.cornerHarris(gray,2,3,0.04)
    #dilating dots
    dst=cv2.dilate(dst,None)
    #drawing dots
    img[dst>0.01*dst.max()]=[0,0,255]
    
    cv2.imshow("Chess Board",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()