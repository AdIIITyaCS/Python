#edge detection by laplacian and sobel method Difference inb/w
# Order of Derivative: Laplacian is a second-order derivative, while Sobel is a first-order derivative.
# Direction Sensitivity: Sobel detects edges in specific directions (horizontal or vertical), whereas Laplacian detects all directions simultaneously.
# Noise Sensitivity: Laplacian is more sensitive to noise due to the use of a second-order derivative, while Sobel incorporates some smoothing to mitigate noise.
import cv2 as cv
import numpy as np
# img= cv.imread('Resources/Photos/cats.jpg')
img= cv.imread('Resources/Photos/Park.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayImage',gray)

#Laplacian 

lap=cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0,ksize=3)
sobely=cv.Sobel(gray,cv.CV_64F,0,1,ksize=3)
combined_sobel=cv.bitwise_or(sobelx,sobely)  #if we combine both the images
 
cv.imshow('SOBEL X',sobelx)
cv.imshow('SOBEL Y',sobely)
cv.imshow('COMBINED_SOBEL',combined_sobel)

#now lets compare with canny edge detector (more clear than above two)
canny= cv.Canny(gray,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)



# Face detection: This only detects the the face. generally we use classifier
# Face recognition: this identifies whose face is it
# Classifier: 1>Harcascade:
#             2>Core local binary Pattern: