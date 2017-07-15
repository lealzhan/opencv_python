import numpy as np
import cv2
from matplotlib import pyplot as plt

#fastNlMeansDenoisingColored
def img():
	img = cv2.imread('lena.jpg')
	#dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	dst = cv2.fastNlMeansDenoisingColored(img,None,6,10,7,21)
	plt.subplot(121),plt.imshow(img)
	plt.subplot(122),plt.imshow(dst)
	plt.show()

#fastNlMeansDenoisingMulti
def video():
	cap = cv2.VideoCapture('vtest.avi')
	# create a list of first 5 frames
	img = [cap.read()[1] for i in xrange(5)]
	# convert all to grayscale
	gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]
	# convert all to float64
	gray = [np.float64(i) for i in gray]
	# create a noise of variance 25
	noise = np.random.randn(*gray[1].shape)*10
	# Add this noise to images
	noisy = [i+noise for i in gray]
	# Convert back to uint8
	noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]
	# Denoise 3rd frame considering all the 5 frames
	#dst = cv2.fastNlMeansDenoisingMulti(noisy, frame_numb, 5, None, 4, 7, 35)
	dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 8, 7, 21)
	plt.subplot(131),plt.imshow(gray[2],'gray')
	plt.subplot(132),plt.imshow(noisy[2],'gray')
	plt.subplot(133),plt.imshow(dst,'gray')
	plt.show()

img()
#video()