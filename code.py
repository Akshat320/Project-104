import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img, "SUN", (100, 100), color = (50, 20, 255), fontFace = (cv2.FONT_HERSHEY_DUPLEX), fontScale = 2.5)

cv2.putText(img, "Mercury", (120, 180), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Venus", (190, 270), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Earth", (290, 270), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Mars", (385, 270), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Jupiter", (510, 70), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Saturn", (780, 120), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Uranus", (965, 130), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)
cv2.putText(img, "Neptune", (1105, 130), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 0.5)

cv2.putText(img, "SOLAR SYSTEM", (350, 400), color = (255, 255, 255), fontFace = (cv2.FONT_HERSHEY_SIMPLEX), fontScale = 2.5)

cv2.imshow("Solar System", img)
cv2.waitKey(0)