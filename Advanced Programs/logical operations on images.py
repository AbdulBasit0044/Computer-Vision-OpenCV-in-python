# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 12:08:16 2018
logical operations on images
@author: AbdulBasit0044
"""
import cv2
import matplotlib.pyplot as plt

def main():
    
    path="images-dataset\\"
    imgpath1 = path + "4.2.06.tiff"
    imgpath2 = path + "4.2.01.tiff"
    #reading images
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    #converting images to RGB from BGR
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    #performing logical opereations on images and creating new images
    img3=cv2.bitwise_not(img1)
    img4=cv2.bitwise_and(img1,img2)
    img5=cv2.bitwise_or(img1,img2)
    img6=cv2.bitwise_xor(img1,img2)
    #creating arrays for images and titles
    titles=['1','2','3','4','5','6']
    images=[img1,img2,img3,img4,img5,img6]
    #loop to load images to pyplot
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()#showing images

if __name__=="__main__":
    main()