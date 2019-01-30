# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 2:08:16 2018
logical operations on images
@author: AbdulBasit0044

resizing images with resize function

"""
import cv2

def main():
    
    #images dataset path
    path="images-dataset\\"
    #storing image path explicitly for every image
    imgpath1 = path + "4.2.06.tiff"
    imgpath2 = path + "4.2.01.tiff"
    #reading images through cv2
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    #converting images to RGB from BGR
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    #performing resizing opereations on images and creating new images
    img3=cv2.resize(img1,None,fx=2,fy=1)
    #displaying images
    cv2.imshow("Output",img3)
    wait=cv2.waitKey(0) & 0xFF
    if (wait == ord('q')):#quit if q is pressed
        cv2.destroyAllWindows()
#calling main
if __name__=="__main__":
    main()