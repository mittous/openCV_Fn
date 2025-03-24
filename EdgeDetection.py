import cv2 

cap = cv2.VideoCapture(0)
cv2.namedWindow("tlfaaaza")
def on_trackbar(val):
    pass
cv2.createTrackbar("up", "tlfaaaza", 0, 255, on_trackbar)
cv2.createTrackbar("down", "tlfaaaza", 0, 255, on_trackbar)


while 1:
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    i = cv2.getTrackbarPos("up", "tlfaaaza")
    j = cv2.getTrackbarPos("down", "tlfaaaza")
    
    edgs = cv2.Canny(gray, i, j)
    cv2.imshow("tlfaaaza", edgs)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()