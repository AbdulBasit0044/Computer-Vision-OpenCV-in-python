# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:37:15 2018

@author: AbdulBasit0044
"""

import cv2
import numpy

img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')

img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
img = cv2.addWeighted(img1,0.7,img2_resized,0.1,0)

cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()