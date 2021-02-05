import cv2

cap = cv2.VideoCapture("video.mp4") 

while True:
    success, img = cap.read() #if cap.read() frame returns success = "True"
    cv2.imshow("Video",img) #Shows frames read by img
    if cv2.waitKey(1) & 0xFF ==ord('q'): #video will stop on pressing "q"
        break
cv2.destroyAllWindows()
