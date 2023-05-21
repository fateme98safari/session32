import cv2

import numpy as np

image=cv2.imread("input/tsukuba_l.png",cv2.IMREAD_GRAYSCALE)

# contrast=cv2.equalizeHist(image,5)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(image)
cv2.imwrite("output/result4.jpg",cl1)
# cv2.imwrite("output/result1.jpg",contrast)