# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:09:24 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np

img=cv2.imread("images-dataset\\circle.jpg",0)
img=cv2.medianBlur(img,7)
color_img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,30,
                            param1=100,param2=30,minRadius=0,maxRadius=0)

circles=np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(color_img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle4
    #cv2.circle(color_img,(i[0],i[1]),2,(0,0,255),3)
    
cv2.imshow("Detected circles",color_img)
cv2.waitKey()
cv2.destroyAllWindows()