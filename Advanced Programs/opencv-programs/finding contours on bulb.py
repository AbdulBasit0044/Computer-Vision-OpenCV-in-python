import cv2
import numpy as np
from imutils import contours
from skimage import measure

def nothing(x):
    pass

def main():
    #reading image
    img=cv2.imread("images-dataset\\house.tiff")
    img=cv2.resize(img,(500,500))
    cv2.imshow("Original Image",img)
    #converting color space
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #blurring to reduce the sharpness of image
    blurred=cv2.GaussianBlur(hsv,(5,5),0)
    #giving thresholding range so that image can be easily traced
    ret,thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)
    #removing noise
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    
    
    cv2.namedWindow("Slider")
    slider=np.zeros((400,700,3),dtype=np.uint8)
    
    cv2.createTrackbar('H low' ,'Slider',0,179,nothing)
    cv2.createTrackbar('H high','Slider',0,179,nothing)
    cv2.createTrackbar('S low' ,'Slider',0,255,nothing)
    cv2.createTrackbar('S high','Slider',0,255,nothing)
    cv2.createTrackbar('V low' ,'Slider',0,255,nothing)
    cv2.createTrackbar('V high','Slider',0,255,nothing)
    
    switch="0:OFF____1:ON"
    cv2.createTrackbar(switch,'Slider',0,1,nothing)
    
    
    while True:
        
        
        
        hl=cv2.getTrackbarPos('H low','Slider')
        hh=cv2.getTrackbarPos('H high','Slider')
        sl=cv2.getTrackbarPos('S low','Slider')
        sh=cv2.getTrackbarPos('S high','Slider')
        vl=cv2.getTrackbarPos('V low','Slider')
        vh=cv2.getTrackbarPos('V high','Slider')
        
        s=cv2.getTrackbarPos(switch,'Slider')
        #setting lower and higher values to which the color detects
        if s==0:
            lower=np.array([0,0,0])
            upper=np.array([180,255,255])
        else:
            lower=np.array([hl,sl,vl])
            upper=np.array([hh,sh,vh])
        #creating mask
        mask = cv2.inRange(thresh, lower, upper)
        #making countours
        _,contours,_ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #drawing contours on image
        cv2.drawContours(img, contours, -1, (0,255,0), 3)
        
        
        #displaying images
        cv2.imshow("Image",img)
        cv2.imshow("Mask",mask)
        k=cv2.waitKey(1) & 0xFF
        if k==27: 
            break
    
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()