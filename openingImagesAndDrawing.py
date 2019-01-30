# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:33:16 2018

@author: AbdulBasit0044
"""
import cv2

img=cv2.imread("Capture.png")
cv2.rectangle(img,(100,100),(510,300),(0,255,0),3)

cv2.imshow("frame",img)
wait=cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()