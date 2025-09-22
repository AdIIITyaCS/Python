#Mask: binary image (typically a matrix of 0s and 1s or 0s and 255s) so 0->pixel off, (1,255)->pixel on
import cv2 as cv
import numpy as np

blank= np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('RectangleImage',rectangle)
cv.imshow('CircleImage',circle)

# #bitwise AND: intersecting region
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise_AND_Image',bitwise_and)

#bitwise OR: intersecting + non-intersecting region
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise_OR_Image',bitwise_or)

#bitwise XOR: non-intersecting region
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_XOR_Image',bitwise_xor)

#bitwise NOT: 
bitwise_not1=cv.bitwise_not(rectangle)
bitwise_not2=cv.bitwise_not(circle)
cv.imshow('Bitwise_NOT_Image1',bitwise_not1)
cv.imshow('Bitwise_NOT_Image2',bitwise_not2)
cv.waitKey(0)