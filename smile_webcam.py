import cv2 as cv

smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)
    for (x, y, w, h) in smiles:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv.imshow("Webcam", frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv.destroyAllWindows()
