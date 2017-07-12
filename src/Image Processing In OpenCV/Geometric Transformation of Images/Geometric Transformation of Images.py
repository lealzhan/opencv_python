# -*- coding: utf-8 -*-
#http://docs.opencv.org/3.2.0/da/d6e/tutorial_py_geometric_transformations.html
import cv2
import numpy as np
import matplotlib.pyplot as plt

#############
## Scaling ##
#############
def Scale():
	img = cv2.imread('messi5.jpg')
	res = cv2.resize( img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
	#OR
	height, width = img.shape[:2]
	res = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)

	cv2.imshow('img',res)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


#################
## Translation ##
#################
def Translation():
	img = cv2.imread('messi5.jpg',0)
	rows,cols = img.shape
	M = np.float32([[1,0,100],[0,1,50]])
	print "translation M:\n",M
	dst = cv2.warpAffine(img,M,(cols,rows))  #仿射变换？(cols,rows) = dst's(width, height)
	cv2.imshow('dst',dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


#################
### Rotation ###
#################
def Rotation():
	img = cv2.imread('messi5.jpg',0)
	rows,cols = img.shape
	M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) #rotates the image by 90 degree with respect to center without any scaling
	dst = cv2.warpAffine(img,M,(cols,rows)) #仿射变换？(cols,rows) = dst's(width, height)
	cv2.imshow('dst',dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


#############################
### Affine Transformation ###
#############################
# In affine transformation, all parallel lines in the original image will still be parallel in the output image. 
# To find the transformation matrix, we need three points from input image and their corresponding locations in 
# output image. Then cv2.getAffineTransform will create a 2x3 matrix which is to be passed to cv2.warpAffine.
def AffineTransformation():
	img = cv2.imread('drawing.png')
	rows,cols,ch = img.shape
	#pts1 : 3 points on input image
	#pts2 : 3 points on input image
	pts1 = np.float32([[50,50],[200,50],[50,200]])
	pts2 = np.float32([[10,100],[200,50],[100,250]])
	#get transformation matrix
	M = cv2.getAffineTransform(pts1,pts2)
	#apply transformation matrix
	dst = cv2.warpAffine(img,M,(cols,rows))
	plt.subplot(121),plt.imshow(img),plt.title('Input')
	plt.subplot(122),plt.imshow(dst),plt.title('Output')
	plt.show()


##################################
### Perspective Transformation ###
##################################
# For perspective transformation, you need a 3x3 transformation matrix. Straight lines will remain straight even 
#after the transformation. To find this transformation matrix, you need 4 points on the input image and corresponding
# points on the output image. Among these 4 points, 3 of them should not be collinear. Then transformation matrix 
#can be found by the function cv2.getPerspectiveTransform. Then apply cv2.warpPerspective with this 3x3 transformation matrix.
def PerspectiveTransformation():
	img = cv2.imread('sudoku.png')
	rows,cols,ch = img.shape
	# pts1 = np.float32([[56,65],	[368,52],	[28,387],	[389,390]])
	# pts2 = np.float32([[0,0],	[300,0],	[0,300],	[300,300]])
	pts1 = np.float32([[72,85],	[489,70],	[35,513],	[519,523]])
	pts2 = np.float32([[0,0],	[300,0],	[0,300],	[300,300]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	dst = cv2.warpPerspective(img,M,(300,300))
	plt.subplot(121),plt.imshow(img),plt.title('Input')
	plt.subplot(122),plt.imshow(dst),plt.title('Output')
	plt.show()


if __name__ == '__main__':
	# Scale()
	# Translation()
	# Rotation()
	# AffineTransformation()
	PerspectiveTransformation()