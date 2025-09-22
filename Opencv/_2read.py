## reading images
import cv2 as cv
# img = cv.imread('Resources/Photos/cat.jpg')  # this function takes images path and returns it as matrix of pixels
# cv.imshow('Cat', img)  #display the image 
# cv.waitKey(0)  # this func waits and display the image for infinite time untill pressed any key 

##reading Resources/Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4') # here capture creates no. of frames to snap full video
while True: #this loops is helpful in reading each frame
  isTrue, frame = capture.read() #read each frame
  cv.imshow('Video', frame)  #display each frame
  if cv.waitKey(20) & 0xFF == ord('d'):  #to not run this infinitely
    break
capture.release() #releasing the capture pointer
cv.destroyAllWindows()  #cancelling the new windows
## some times error like (-215:assertion failed) shows because of wrong path or not finding any frame
