import cv2 as cv
# img = cv.imread('Resources/Photos/cat.jpg')
img = cv.imread('Resources/Photos/Myphoto.jpg')
cv.imshow('Cat',img)

# #converting bgr image to grayscale(black & white) image
# grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('GrayScale',grey) 

# #blurring a image (reduces problems related to noise,camera sensor)
# blur= cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) # here the 3x3 dimension to 7x7 increases the blurrings
# blur= cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('BlurImage',blur)

#Edge cascading(finding the edges in the images),Canny Edge Detection is a popular algorithm used to detect edges in images. (<125 not edge, >175 edge and inb/n is considered only the connected edge intensity is >175)
canny=cv.Canny(img, 125, 175)  
# canny=cv.Canny(blur, 125, 175) # here when blur image is passed then edge creating is low as compare to img
cv.imshow('EdgeOfImage',canny)

# #dilating the canny Edge image (dilation is an image processing operation that makes the bright regions (typically white in a binary image) larger. It is often used to enhance features like edges or fill in gaps in an image)
# #In signature verification, dilation can help make thin lines of a signature thicker, improving the recognition of the signature's overall shape and ensuring that gaps in pen strokes are filled
# dilated=cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('DilatedImage',dilated)

##Eroding the dilated image (Erosion reduces the size of the white regions in a binary image. It does this by eroding away the boundaries of the foreground (bright) regions.)
# eroded=cv.erode(dilated,(7,7),iterations=3)
# cv.imshow('ErodedImage',eroded)


# #Resize 
# resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA) #shrinking the image
# cv.imshow('ResizeImage',resize)

#Cropping (to take part of a image)
# cropped=img[50:200,200:400]
# cv.imshow('CroppedImage',cropped)
cv.waitKey(0) 