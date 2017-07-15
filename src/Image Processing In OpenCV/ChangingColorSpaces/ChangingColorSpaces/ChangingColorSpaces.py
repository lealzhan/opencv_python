# 0. cvtColor
# 1. In HSV, it is more easier to represent a color than in BGR color-space.
import cv2
import numpy as np

def object_tracking():
	# cap = cv2.VideoCapture(0)
	cap = cv2.VideoCapture('vtest.avi')
	while(1):
		# Take each frame
		ret, frame = cap.read()
		if ret==False : 
			break
		# Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		# define range of blue color in HSV
		lower_blue = np.array([110,50,50])
		upper_blue = np.array([130,255,255])
		# Threshold the HSV image to get only blue colors
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(frame,frame, mask= mask)
		cv2.imshow('frame',frame)
		cv2.imshow('mask',mask)
		cv2.imshow('res',res)
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
	cv2.destroyAllWindows()

#hsv range in opencv [0,179] [0,255] [0,255]
#take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.
def ConvertRGB2HSV(r=255,g=255,b=255):
	hsv = cv2.cvtColor(np.uint8([[[ b, g, r]]]), cv2.COLOR_BGR2HSV)
	print "rgb",r,g,b, " => hsv", hsv
	return hsv

ConvertRGB2HSV(0,0,255)
ConvertRGB2HSV(0,255,0)
ConvertRGB2HSV(255,0,0)
object_tracking()


