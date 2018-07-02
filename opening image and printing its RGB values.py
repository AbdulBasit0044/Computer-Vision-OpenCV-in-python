import cv2

img=cv2.imread("ronaldo.jpg")

#cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
#cv2.imshow("frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

px=img[100,100]
print (px)

blue=img[100,100,0]
red=img[100,100,2]
green=img[100,100,1]

print(blue)
print(green)
print (red)

red1=img.item(100,100,2)
print(red1)
img.itemset((100,100,2),100)
print(red1)
red1=img.item(100,100,2)
print(red1)