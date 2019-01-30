# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:14:28 2018
Finding pixels with corners using Shi-Thomsi algorithm
@author: AbdulBasit0044
"""

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
    img=cv2.resize(img,(600,600))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detecting corners 25 is the numbers of best pixels we want to show and 0.8 is the quality
    corners=cv2.goodFeaturesToTrack(gray,25,0.8,1)
    corners=np.uint0(corners)    
    #drawing
    for i in corners:
        x,y=i.ravel()
        cv2.circle(img,(x,y),3,(0,0,255),-1)
    #showing images
    cv2.imshow("Chess Board",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()