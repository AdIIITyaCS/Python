#Mask: It involves creating a mask, which is typically a binary image (black and white) that defines which parts of the original image should be kept and which should be ignored.
import cv2 as cv
import numpy as np

img=cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('BlankImage',blank)

circle=cv.circle(blank.copy(),(img.shape[1]//2 + 45,img.shape[0]//2),100,255,-1)
cv.imshow('CircleImage',circle)


rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
wierd_shape =cv.bitwise_and(circle,rectangle)
cv.imshow('WierdShape',wierd_shape)

masked = cv.bitwise_and(img,img,mask=wierd_shape)
cv.imshow('Wierd_Shaped_MaskedImage',masked)

cv.waitKey(0)