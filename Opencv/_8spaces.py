# how to switch between color spaces(array of color pixels) like rgb,gray scale...
#conversion is possible only through bgr


import cv2 as cv
img= cv.imread('Resources/Photos/Park.jpg')
cv.imshow('ParkImage',img)

#since opencv percieves the images as bgr but outside it images are percieved in matplot as rgb so nxt two line will show the difference of bgr and rgb 
# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.show()



# BGR TO GREY SCALE
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayImage',gray)

# # BGR TO HSB
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSVImage',hsv)

# # BGR TO L*a*b
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LABImage',lab)

# #BGR to RGB
# rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('RGBImage',rgb)
# plt.imshow(rgb)
# plt.show()

# greyscale to bgr to hsb
grey_bgr= cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
cv.imshow('Grey-->BGRImage',grey_bgr)

cv.waitKey(0)