# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:14:43 2018

@author: AbdulBasit0044
"""

import cv2

def main():
    
    imgpath="C:\\opencv341\\opencv\\sources\\images-dataset\\lena_color_256.tiff"
    img=cv2.imread(imgpath)
    
    cv2.imshow('frame',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()