import cv2 as cv
# img=cv.imread('Resources/Photos/lady.jpg')
# cv.imshow('Lady',img)

# img=cv.imread('Resources/Photos/group 2.jpg')
# cv.imshow('Group2',img)

img=cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Group1',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayImage',gray)

# here we use the xml file
haar_cascade= cv.CascadeClassifier('_17haar_face.xml') # this will read xml file store it in haar_cascade

faces_rect= haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1) #as we increase minNeigh.. the sensitivity also increases
print(f'No of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
  cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2) #what to do for msking circle on image

cv.imshow('Detected faces',img)

cv.waitKey(0)