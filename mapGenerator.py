import cv2
import numpy as np

height = 1080
width = 1920

image = np.zeros((height,width,3), np.uint8)

for x in range(height):
	for y in range(width):
		if x > -0.001*y**2 + 2.15*y - 200:
		# if x > -0.6*y + 1100:
			image[x,y,0] = 255
			image[x,y,1] = 255
			image[x,y,2] = 255

cv2.imshow('Output', image)
cv2.imwrite('/home/wojtryb/Programowanie/python/game2d/bg2.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

quit()