import cv2

img = cv2.imread("lenna.png")

#converts RGB to Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Kernal size to blur image is (5x5) and sigma = 0
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)
#edge detection using Canny
#increasing Threshold value reduces edges
imgCanny = cv2.Canny(img, 150, 200)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)

cv2.waitKey(0)