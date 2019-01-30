# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:14:43 2018

@author: AbdulBasit0044
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath="images-dataset\\lena_color_256.tif"
    img=cv2.imread(imgpath,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('Color image with default colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    

    #cv2.imshow('frame',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()