# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:09:58 2018

@author: AbdulBasit0044
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:04:31 2018

@author: AbdulBasit0044
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:30:35 2018
This program read some image from directory and then split it into its RGB colorspaces
then merge RGB colorspace to make original image again and then show images in different colorspaces
@author: AbdulBasit0044
"""

import cv2
import matplotlib.pyplot as plt

def emptyFunction():
    pass

def main():
    #specifying path of dataset
    path="images-dataset\\"
    #giving different images names
    imgpath1=path + "4.2.01.tiff"
    #reading images through opencv funtion
    img1=cv2.imread(imgpath1)
    #converting image color scheme because open cv read images in BGR format but
    #we want to show in RGB format
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    #splitting images with respect to color
    r,g,b=cv2.split(img1)
    #creating array to store data
    titles=['Original Image','Red','Green','Blue']
    #merging red green blue colors and making original image
    images=[cv2.merge((r,g,b)),r,g,b]
    #displaying all images using loop
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()#show the pallete in which images are placed
    #calling main function
if __name__=="__main__":
    main()