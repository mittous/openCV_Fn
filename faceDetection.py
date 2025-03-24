import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while 1:
    
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 8)

    for (q,w,e,r) in faces:
        cv2.rectangle(frame, (q,w), (q+e, w+r), (232,133,23), 2)

    cv2.imshow("tlfaz", frame)
    if cv2.waitKey(1) == 27:
        break



cap.release()
cv2.destroyWindow()