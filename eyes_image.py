import cv2 as cv

eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
img = cv.imread('img.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in eyes:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow("Imagey", img)
cv.waitKey(0)
cv.destroyAllWindows()
