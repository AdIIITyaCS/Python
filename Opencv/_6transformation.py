import cv2 as cv
import numpy as np


img= cv.imread('Resources/Photos/Myphoto.jpg')
# img= cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Myphoto',img)


#translation (moving an image up,down or other)
# -x = left
# x = right
# -y = up
# y = down
def translate(img,x,y):
  transMat = np.float32([[1,0,x],[0,1,y]])
  dimension = (img.shape[1],img.shape[0])
  return cv.warpAffine(img,transMat, dimension)


translated = translate(img, -100,-100)
cv.imshow('TranslatedImage',translated)


#rotation 
def rotate(img,angle, rotPoint=None):
  (height,width) = img.shape[:2]
  if rotPoint is None:
    rotPoint= (width//2,height//2)

  rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
  dimension = (width,height)
  return cv.warpAffine(img, rotMat,dimension)

rotated=rotate(img, -45)
cv.imshow('RotatedImage',rotated)

#flipping
flip=cv.flip(img, -1)
cv.imshow('FlipImage',flip) 

cv.waitKey(0)