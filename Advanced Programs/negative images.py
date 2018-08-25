"""
Created on Wed Jul 18 15:30:35 2018
This program read some image from directory and make negative of images in color or 
gray format
@author: AbdulBasit0044
"""

import cv2
import matplotlib.pyplot as plt

def main():
    #specifying path of dataset
    path="images-dataset\\"
    #giving different images names
    imgpath1=path + "4.2.06.tiff"
    #reading images through opencv funtion
    img=cv2.imread(imgpath1,1)
    #converting image color scheme because open cv read images in BGR format but
    #we want to show in RGB format
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #making negatives of color and gray image
    img3=abs(255-img1)
    img4=abs(255-img2)
    #creating array to store data
    titles=['Color Image','Gray Scale','Color-Negative','Grayscale-Negative']
    images=[img1,img2,img3,img4]
    #displaying all images using loop
    for i in range(4):
        plt.subplot(2,2,i+1)
        if (i%2!=0):
            plt.imshow(images[i],cmap='gray')
        else:
            plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()#show the pallete in which images are placed
    #calling main function
if __name__=="__main__":
    main()