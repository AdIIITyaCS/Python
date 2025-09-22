#smoothing is done only if there is a lot of noise due to camera sensors,picture taken in too much lightning
# by using the blurry method we smoothen(reduce the noise)
# window: the small portion of the image 
# kernel: the small portion of the image that is used to blur the image
import cv2 as cv
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

#1> Average Blur: if we take 3x3 window then average of all other is blocks is given to centre and this slides till end of the i/p image
average = cv.blur(img,(3,3))  # as we increase the 3x3 to 7x7(not  recommended) blurred behaviour increases
# average = cv.blur(img,(7,7))
cv.imshow('AverageImage',average)  

#2> Gaussian Blur: same as average blur but (average of corner blocks = centre) 
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('GaussImage',gauss)

#3> Median Blur: median of all other is blocks is given to centre and this slides till end of the i/p image
median = cv.medianBlur(img,3) # assumes medianblur image of 3x3 
cv.imshow('MedianBlurImage',median)

#4> Bilateral Blur: this retains the edges of modified image irrespective from others (BEST from others)
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateralBlurImage',bilateral)
cv.waitKey(0)