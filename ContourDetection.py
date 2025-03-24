import cv2 

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    _, frame2 = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    edges = cv2.Canny(gray, 50, 150)
    
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoursCanny, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    cv2.drawContours(frame2, contoursCanny, -1, (0, 255, 0), 2)

    cv2.imshow("tlfaaaza", frame)
    cv2.imshow("tlfasaaza", frame2)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()