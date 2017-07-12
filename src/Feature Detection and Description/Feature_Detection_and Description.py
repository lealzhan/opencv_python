#http://docs.opencv.org/3.2.0/db/d27/tutorial_py_table_of_contents_feature2d.html

import cv2
import numpy as np
from matplotlib import pyplot as plt


def Harris_Corner_Detection():
	# filename = 'chessboard.png'
	filename = 'blox.jpg'
	img = cv2.imread(filename)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)
	dst = cv2.cornerHarris( gray, 2, 3, 0.04)
	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)
	# Threshold for an optimal value, it may vary depending on the image.
	img[dst>0.01*dst.max()]=[0,0,255]
	cv2.imshow('dst',img)
	if cv2.waitKey(0) & 0xff == 27:
	    cv2.destroyAllWindows()

def Shi_Tomasi_Corner_Detector():
	img = cv2.imread('blox.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
	corners = np.int0(corners)
	for i in corners:
	    x,y = i.ravel()
	    cv2.circle(img,(x,y),3,255,-1)
	plt.imshow(img),plt.show()

#patented
def SIFT():
	# img = cv2.imread('home.jpg')
	img = cv2.imread('blox.jpg')
	gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	sift = cv2.xfeatures2d.SIFT_create()
	kp = sift.detect(gray,None)
	img=cv2.drawKeypoints(gray,kp,img)
	cv2.imwrite('sift_keypoints.jpg',img)

#patented
def SURF():
	pass

#fast in embeded
def FAST():
	img = cv2.imread('blox.jpg',0)
	# Initiate FAST object with default values
	fast = cv2.FastFeatureDetector_create()
	# find and draw the keypoints
	kp = fast.detect(img, None)
	img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
	# Print all default params
	print "Threshold: ", fast.getThreshold()
	print "nonmaxSuppression: ", fast.getNonmaxSuppression()
	print "neighborhood: ", fast.getType()
	print "Total Keypoints with nonmaxSuppression: ", len(kp)
	cv2.imwrite('fast_true.png',img2)
	# Disable nonmaxSuppression
	fast.setNonmaxSuppression(0)
	kp = fast.detect(img,None)
	print "Total Keypoints without nonmaxSuppression: ", len(kp)
	img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
	cv2.imwrite('fast_false.png',img3)


#lower memory, fast matching
def Brief():
	pass

#free
def ORB():
	img = cv2.imread('blox.jpg',0)
	# Initiate ORB detector
	orb = cv2.ORB_create()
	# find the keypoints with ORB
	kp = orb.detect(img,None)
	# compute the descriptors with ORB
	kp, des = orb.compute(img, kp)
	# draw only keypoints location,not size and orientation
	img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
	plt.imshow(img2), plt.show()

if __name__ == '__main__':
	# Harris_Corner_Detection()
	# Shi_Tomasi_Corner_Detector()
	#SIFT() # not working
	# FAST()
	ORB()