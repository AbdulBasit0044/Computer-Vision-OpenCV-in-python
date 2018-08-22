# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:33:13 2018
Thresholding live webcam feed
@author: AbdulBasit0044
"""
import cv2

def main():
    #capturing feed from webcam
    cap=cv2.VideoCapture(0)
    #if feed captured succesfully then read frame
    if cap.isOpened():
        ret, frame=cap.read()
    else:
        False
        
    #until frames are reading from feed continue loop
    while ret:
        #reading frame from feed
        ret,frame=cap.read()
        #flipping frame, not to get mirrored image
        imo=cv2.flip(frame,1)#this is flipped frame
        #setting low threshold value
        th=127
        #setting high threshold value
        max_val=255
        #applying different thresholding algorithms
        ret,o1=cv2.threshold(imo,th,max_val,cv2.THRESH_BINARY)
        ret,o2=cv2.threshold(imo,th,max_val,cv2.THRESH_BINARY_INV)
        ret,o3=cv2.threshold(imo,th,max_val,cv2.THRESH_TOZERO)
        ret,o4=cv2.threshold(imo,th,max_val,cv2.THRESH_TOZERO_INV)
        ret,o5=cv2.threshold(imo,th,max_val,cv2.THRESH_TRUNC)
        o6=cv2.Canny(imo, 120, 170)
        #showing images
        cv2.imshow("Binary",o1)
        cv2.imshow("Binary Inv",o2)
        cv2.imshow("Binary Tozero",o3)
        cv2.imshow("Binary Tozero Inv",o4)
        cv2.imshow("Binary Trunc",o5)
        cv2.imshow("Canny edge detection",o6)
        #setting ESC key to break loop
        if cv2.waitKey(1)==27:
            break
    #when loops breaks then destroying windows
    cv2.destroyAllWindows()
#calling main
if __name__=="__main__":
    main()