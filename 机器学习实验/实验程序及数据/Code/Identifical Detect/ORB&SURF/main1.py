import cv2

img = cv2.imread('111.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ORB = cv2.ORB_create()
kp = ORB.detect(gray, None)
img2 = cv2.drawKeypoints(img, kp, (0, 0, 255))

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img2)
cv2.imwrite('111.jpg', img2)
cv2.waitKey(0)
