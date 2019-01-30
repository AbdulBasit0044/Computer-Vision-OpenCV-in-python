# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:45:20 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import time

def main():
    
    #giving live stream to program
    windowName="Live feed window"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)
    #checking if live stream is coming or not
    if cap.isOpened():
        ret, frame=cap.read()
    else:
        ret=False
    #extracting shape of image(extracting rows,columns and channels numbers), this is color image so 3 parameters is used
    #channels show that if the image is colored or not
    rows,columns,channels=frame.shape
    #giving starting angle and scale of image
    angle=0
    scale=0.1
    
    while True:
        #making sure that frames from stream is coming continuously
        ret,frame=cap.read()
        #ressetting angle
        if angle==360:
            angle=0
        #making zooming effect
        if scale<2:
            scale=scale+0.1
        if scale>=2:
            scale=0.1
        #making rotation matrix
        R=cv2.getRotationMatrix2D((columns/2,rows/2),angle,scale)
        #applying rotation matrix
        output=cv2.warpAffine(frame,R,(columns,rows))
        #showing webcap feed
        cv2.imshow(windowName,output)
        angle=angle+1#incrementing so that image could rotate
        time.sleep(0.01)
        #wait for ESC key to stop progran
        if cv2.waitKey(1)==27:
            break
        #destroying window
    cv2.destroyWindow(windowName)
    #calling main function
if __name__ =="__main__":
    main()