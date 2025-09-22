# Contours are the outlines or boundaries of objects, and detecting them helps emphasize the edges and unique characteristics of each signature
#use the canny method first then find the contours  
#don't use the threshold first then contours

import cv2 as cv
import numpy as np
img = cv.imread('Resources/Photos/cats.jpg')
# img = cv.imread('Resources/Photos/Myphoto.jpg')
# img = cv.imread('Resources/Photos/sign.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape , dtype='uint8') # dtype is datatype of image  and 500X500 resolution with 3 rgb colors
cv.imshow('BlankImage',blank)


grey= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GreyCats',grey)



#blurring a image (reduces problems related to noise,camera sensor)
blur= cv.GaussianBlur(grey,(5,5),cv.BORDER_DEFAULT) # here the 3x3 dimension to 7x7 increases the blurrings
cv.imshow('BlurImage',blur)


#Edge cascading(finding the edges in the images),Canny Edge Detection is a popular algorithm used to detect edges in images. (<125 not edge, >175 edge and inb/n is considered only the connected edge intensity is >175)
# canny=cv.Canny(img, 125, 175)  
canny=cv.Canny(blur, 125, 175)  
cv.imshow('EdgeOfImage',canny)

# ret,thresh = cv.threshold(grey,125,255,cv.THRESH_BINARY) #threshold binaries the image into either black(<125) or white(>255)
# cv.imshow('ThresholdImage',thresh)

# contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#cv.RETR_LIST: this return list of the contours in the image
#hierarchies: rectangle[circle{square(rhombus)}] inside inside inside ........
#cv.CHAIN_APPROX_NONE: returns all the coordinates of the image line line, rectangle.... 
#cv.CHAIN_APPROX_SIMPLE: returns all essential coordinates of the image .... 
print(f'{len(contours)} contour found') # since only finding the edges from canny is too large so use it after blur 

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('ContourDrawn',blank)

cv.waitKey(0)