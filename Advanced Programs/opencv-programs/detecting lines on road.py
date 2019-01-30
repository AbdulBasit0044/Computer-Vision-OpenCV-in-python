# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:31:49 2018

@author: AbdulBasit0044
"""

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

def main():
    
    video=cv2.VideoCapture("images-dataset\\road_car_view.mp4")

    while True:
        #reading frame
        ret,frame=video.read()
        #applying gaussian blur so that getting better result after smoothing image
        frame=cv2.GaussianBlur(frame,(7,7),0)
        #converting hsv colorspace so that detect whatever color we want from frame
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #setting lower and upper threshols for color to detect
        lower_yellow=np.array([10,94,140])
        upper_yellow=np.array([40,255,255])
        #creating mask
        mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
        #detecting edges
        edges=cv2.Canny(mask,75,150,)
        #making hough lines
        lines=cv2.HoughLinesP(edges, 1, np. pi/180,50,  maxLineGap=50)
        #drawing lines
        if lines is not None:
            for line in lines:
                x1,y1,x2,y2=line[0]
                cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 3)
        #showing frame with drawn lines
        cv2.imshow("frame",frame)
        #exit if ESC press
        key=cv2.waitKey(25)
        if key==27:
            break
    #release video from memory    
    video.release()
    cv2.destroyAllWindows()

#calling main
if __name__=="__main__":
    main()