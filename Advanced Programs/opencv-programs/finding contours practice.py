# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:42:11 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([100,100,100])
    upper=np.array([200,200,200])
    mask=cv2.inRange(hsv,lower,upper)
    
    cv2.imshow("Camera",frame)
    cv2.imshow(" Mask",mask)
    
    key=cv2.waitKey()
    if key==27:
        break
    
    
    
    
cap.release()
cv2.destroyAllWindows()