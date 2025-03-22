import cv2

img = cv2.imread("chess.png")

while 1:
    cv2.imshow("tlfaza", img)
    if cv2.waitKey(19) == 27:
        break

cv2.destroyAllWindows()