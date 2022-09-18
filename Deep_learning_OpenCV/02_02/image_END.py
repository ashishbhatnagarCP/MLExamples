import numpy as np
import cv2
img = cv2.imread('../images/devon.jpg')
#print(img.shape)

b = img[:,:,0]# here 0 represent B of BRG
print(b)
g = img[:,:,1]# here 1 represent R of BRG
r = img[:,:,2]# here 2 represent G of BRG

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
