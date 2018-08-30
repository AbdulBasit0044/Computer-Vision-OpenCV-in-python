# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:08:42 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

original_image=cv2.imread("images-dataset//goalkeeper.jpg")
cut=cv2.imread("images-dataset//pitch_ground.jpg")


hsv_original=cv2.cvtColor(original_image,cv2.COLOR_BGR2HSV)
hsv_cut=cv2.cvtColor(cut,cv2.COLOR_BGR2HSV)

hue,saturation,value=cv2.split(hsv_cut)

cut_hist=cv2.calcHist([hsv_cut],[0,1],None,[180,256],[0,180,0,256])
mask=cv2.calcBackProject([hsv_original],[0,1],cut_hist,[0,180,0,256],1)

kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask=cv2.filter2D(mask,-1,kernel)
_, mask=cv2.threshold(mask,30,255,cv2.THRESH_BINARY)
mask=cv2.merge((mask,mask,mask))
result=cv2.bitwise_and(original_image,mask)


#plt.imshow(cut_hist)
#plt.show()
cv2.imshow("Mask",mask)
cv2.imshow("Original Images",result)
cv2.imshow("Collar image",cut)
cv2.waitKey()
cv2.destroyAllWindows()


