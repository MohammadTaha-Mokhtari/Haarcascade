import cv2 as cv

smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')
img = cv.imread('img.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)
for (x, y, w, h) in smiles:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
