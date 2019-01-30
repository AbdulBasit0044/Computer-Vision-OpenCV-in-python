# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:21:25 2018

@author: AbdulBasit0044
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:48:33 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    img=cv2.imread("images-dataset\\lines.png",1)
    img=cv2.resize(img,(500,350))
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray,75,150)
    
    lines=cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=120)
    
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)
    
    
    cv2.imshow("Original Image",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    
if __name__=="__main__":
    main()