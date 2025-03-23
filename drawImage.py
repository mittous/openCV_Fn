import cv2

img = cv2.imread("chess.png")

while 1:
    
    cv2.line(img, (30, 50), (90,30), (0, 255,5), 4)
    cv2.rectangle(img, (40,58), (100, 500), (123,156,53), 9)
    cv2.circle(img, (500,509), 90, (187,0,233), 8)
    
    cv2.putText(img, "write on the image", (400, 300), 2, 4, (164,200,7), 2)
    cv2.imshow("tlfazadatani",img)
    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()