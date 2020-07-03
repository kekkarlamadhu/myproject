#importng the numpy module
import numpy as np
#importing the cv2 module.
import cv2
#read the image with a call to the imread function
img = cv2.imread(r"image.jpeg")
#Canny edge detection
edges = cv2.Canny(img,180,200,apertureSize = 3)
#it detect lines in an image.
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=215, minLineLength=50)
for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("linesDetected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
