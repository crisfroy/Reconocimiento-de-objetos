import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

bottleClassif = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bot = bottleClassif.detectMultiScale(gray, scaleFactor=5, minNeighbors=91, minSize=(50, 50)) 

    for (x, y, w, h) in bot:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Botella Buen Estado', (x, y-10), 2, .8, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
