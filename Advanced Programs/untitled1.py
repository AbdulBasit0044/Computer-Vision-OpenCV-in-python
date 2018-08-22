# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 12:47:20 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np

def main():
    img=np.zeros((512,512,3),np.uint8)
    
    cv2.imshow("Lena",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()