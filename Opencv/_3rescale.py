# reducing the images size helps the model to get less computational strain
import cv2 as cv

def rescaleFrame(frame,scale=.75):  # it will rescale the video or image
  width = int(frame.shape[1] * scale) # here frame1 for width and frame0 for height which is scaled by 75%
  height =int(frame.shape[0] * scale)
  dimension = (width,height)
  return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/cat.jpg')  # this function takes images path and returns it as matrix of pixels
cv.imshow('Cat', img)  #display the image 
resized_image=rescaleFrame(img)
cv.imshow('Resized Image',resized_image)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
  isTrue, frame = capture.read()
  frame_resized=rescaleFrame(frame,scale=.2)
  cv.imshow('Video', frame)
  cv.imshow('Video Resized', frame_resized)
  if cv.waitKey(20) & 0xFF == ord('d'):
    break
capture.release()
cv.destroyAllWindows()