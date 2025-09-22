import cv2 as cv
import numpy as np

#creating blank image
blank = np.zeros((500,500,3) , dtype='uint8') # dtype is datatype of image  and 500X500 resolution with 3 rgb colors
cv.imshow('BlankImage',blank)

# #paint the blank image
# blank[200:300, 300:400]=0,0,255   #in blank image the paintedRed image will display from (200-299),(300,399)
# cv.imshow('PaintedRed', blank)

# #draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=2) # RedRectangle image will display from (0,0) to (250,250) with red color
# cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=cv.FILLED) # cv.filled the figure with red color filled
# cv.imshow("RedRectangle",blank)

#draw a circle
# cv.circle(blank,(150,150),50,(0,0,255),thickness=-1)  #-1 or cv.FILLED shows circle filled with green color
# cv.circle(blank,(150,150),50,(0,0,255),thickness=cv.FILLED)  #-1 shows filled circle
# cv.imshow('GreenCircle',blank)

# #draw a line
# cv.line(blank,(0,0),(250,250),(0,0,255),thickness=2)
# cv.imshow('GreenLine',blank)

#write a text
# cv.putText(blank,'Hello',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=1) # draw text"Hello" from coordinate 0,225 with fontstyle and fontscale 1
cv.imshow('Text',blank)


# img=cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)
cv.waitKey(0)