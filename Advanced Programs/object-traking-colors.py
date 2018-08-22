# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:02:14 2018

@author: AbdulBasit0044
"""

#tracking objects on the basis of color

import cv2
import numpy as np

def main():
    
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame=cap.read()
    else:
        ret=false
        
    while ret:
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        #blue color tracking
        blow=np.array([100,100,50])
        bhigh=np.array([140,255,255])
        bimage_mask=cv2.inRange(hsv,blow,bhigh)
        boutput=cv2.bitwise_and(frame,frame,mask=bimage_mask)
        #green color tracking
        glow=np.array([20,70,70])
        ghigh=np.array([80,255,255])
        gimage_mask=cv2.inRange(hsv,glow,ghigh)
        goutput=cv2.bitwise_and(frame,frame,mask=gimage_mask)
        #Red color tracking
        rlow=np.array([140,100,10])
        rhigh=np.array([180,255,255])
        rimage_mask=cv2.inRange(hsv,rlow,rhigh)
        routput=cv2.bitwise_and(frame,frame,mask=rimage_mask)
        
        #cv2.imshow("Original Feed",frame)
        #cv2.imshow("Image mask",image_mask)
        cv2.imshow("Blue Color Tracking",boutput)
        cv2.imshow("Green Color Tracking",goutput)
        cv2.imshow("Red Color Tracking",routput)
    
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()
    
if __name__=='__main__':
    main()
