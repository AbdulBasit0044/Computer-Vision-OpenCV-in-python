# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 13:01:14 2018

@author: AbdulBasit0044
"""

import cv2
import numpy as np


def main():
    
    img1=cv2.imread("images-dataset\\the_book_thief.jpg")
    img2=cv2.imread("images-dataset\\me_holding_book.jpg")
    
    #sift=cv2.xfeatures2d.SIFT_create()
    #surf=cv2.xfeatures2d.SURF_create()
    orb=cv2.ORB_create()
    #getting keypoints
    keypoints1, descriptors1=orb.detectAndCompute(img1,None)
    keypoints2, descriptors2=orb.detectAndCompute(img2,None)
    #drawing keypoints
    img1=cv2.drawKeypoints(img1, keypoints1, None)
    
    #Brute force to match detected features
    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches=bf.match(descriptors1,descriptors2)
    matches=sorted(matches,key=lambda x:x.distance)
    
    matching_result=cv2.drawMatches(img1,keypoints1,img2,keypoints2,matches[:20],None)
    #showing images
    cv2.imshow("Book",img1)
    cv2.imshow("Holding Book",img2)
    cv2.imshow("Matching Result",matching_result)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()