# Thresholding(Simple thresholding and adaptive) is used to convert an image to a binary image based on intensity values.binary image (typically a matrix of 0s and 1s or 0s and 255s) so 0->pixel off, (1,255)->pixel on. Here we set a thresholded(th) intensity if particular pixel is greater than (th) then it is set to 255 or white otherwise 0or black
import cv2 as cv
img= cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayImage',gray)
# # Simple thresholding(here we deal with gray scale image)
# # thresh:This is the resultant binary image. It has pixel values either 0 or 255 depending on whether they were below or above the threshold value.
# # threshold:This is the threshold value used in the operation, which is 150 in this case as <150 we get more whiter image otherwise >150 we get blacker one
# threshold , thresh =  cv.threshold(gray,100,255,cv.THRESH_BINARY) # .BINARY returns 0 or 255
# cv.imshow('SIMPLE THRESHOLDED',thresh)
# threshold , thresh_inv =  cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # .BINARY returns 0 or 255
# cv.imshow('SIMPLE THRESHOLDED INVERSE',thresh_inv)

#Adaptive thresholding( in above case we have to manually type the threshold value but here we let the computer find the optimal (th) to get rid of it)
adaptive_thresh= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,9)
# adaptive_thresh= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholded',adaptive_thresh)
cv.waitKey(0)