import cv2

cap = cv2.VideoCapture(0) # captures video through webcam
cap.set(3, 640) #sets frame width(id =3) to 640
cap.set(4, 480) #sets frame height(id =4) to 480
cap.set(10, 100) #sets frame brightness to 100


while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()