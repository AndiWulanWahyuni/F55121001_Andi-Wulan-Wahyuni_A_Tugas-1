import cv2
import numpy as np

img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Lena Original", img)
cv2.imshow("Gambar Lena Grayscale", gray)

cv2.waitkey(0)
cv2.destroyAllWindows()