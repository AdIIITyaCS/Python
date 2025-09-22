#Splitting and merging color of a image
#when there is high intensity in particular region then it will show white if not then dark
import cv2 as cv
import numpy as np


img= cv.imread('Resources/Photos/Park.jpg')
cv.imshow('ParkImage',img)

# If the image is a color image (e.g., RGB), img.shape will return (height, width, channels).
# If the image is a grayscale image, it will return (height, width).
blank = np.zeros(img.shape[:2] , dtype='uint8') # dtype is datatype of image and img.shape[:2] extracts only the first two values from the tuple
cv.imshow('BlankImage',blank)

b,g,r = cv.split(img) #b,g,r is diff. color channnels in which image is divided 

blue=cv.merge([b,blank,blank]) # showing blue component respectively
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('BluePart',blue)
cv.imshow('GreenPart',green)
cv.imshow('RedPart',red)

print(img.shape) # shape is 3 due to 3 color
print(b.shape) #shape is 1 due to one color
print(g.shape)
print(r.shape)

merged =cv.merge([r,g,b])
cv.imshow('MergedImage',merged) 
cv.waitKey(0)