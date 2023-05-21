import cv2
import numpy as np

image=cv2.imread("input/images.jpg",cv2.IMREAD_GRAYSCALE)
kernel=np.array([[-1,0,0],
                 [0,1,0],
                 [0,0,1]])

result=cv2.filter2D(image,-1,kernel)

cv2.imwrite("output/result5.jpg",result)
