import cv2
import numpy as np

img=cv2.imread('D:\python\cards.png')

width,height = 250,350
pts1 = np.float32([[424,190],[1010,183],[410,962],[1010,955]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Image',img)
cv2.imshow('Output Image',imgOutput)

cv2.waitKey(0)