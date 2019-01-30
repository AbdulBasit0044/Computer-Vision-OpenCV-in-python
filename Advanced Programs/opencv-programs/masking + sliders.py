import cv2
import numpy as np

def nothing(x):
    pass

def main():
    #reading video
    cap=cv2.VideoCapture(0)
    #converting color space
    #img=cv2.imread("images-dataset\\bulbs.jpg")
    #blurring to reduce the sharpness of image
    
    
    
    cv2.namedWindow("Slider")
    #slider=np.zeros((400,700,3),dtype=np.uint8)
    
    cv2.createTrackbar('H low' ,'Slider',0,179,nothing)
    cv2.createTrackbar('H high','Slider',179,179,nothing)
    cv2.createTrackbar('S low' ,'Slider',0,255,nothing)
    cv2.createTrackbar('S high','Slider',255,255,nothing)
    cv2.createTrackbar('V low' ,'Slider',0,255,nothing)
    cv2.createTrackbar('V high','Slider',255,255,nothing)
    
    switch="0:OFF____1:ON"
    cv2.createTrackbar(switch,'Slider',0,1,nothing)
    
    
    while True:
        
        
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    
        
        #blurred=cv2.GaussianBlur(hsv,(5,5),0)
        #giving thresholding range so that image can be easily traced
        #ret,thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)
        #removing noise
        #thresh = cv2.erode(thresh, None, iterations=2)
        #thresh = cv2.dilate(thresh, None, iterations=4)
        
        hl=cv2.getTrackbarPos('H low','Slider')
        hh=cv2.getTrackbarPos('H high','Slider')
        sl=cv2.getTrackbarPos('S low','Slider')
        sh=cv2.getTrackbarPos('S high','Slider')
        vl=cv2.getTrackbarPos('V low','Slider')
        vh=cv2.getTrackbarPos('V high','Slider')

        lower=np.array([hl,sl,vl])
        upper=np.array([hh,sh,vh])
        #creating mask
        mask = cv2.inRange(hsv, lower, upper)
        #making countours
        _,contours,_ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #drawing contours on image
        cv2.drawContours(frame, contours, -1, (0,255,0), 3)
        
        
        #displaying images
        cv2.imshow("Image",frame)
        cv2.imshow("Mask",mask)
        k=cv2.waitKey(1) & 0xFF
        if k==27: 
            break
    
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()