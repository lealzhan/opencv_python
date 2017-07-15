import cv2
import numpy as np
from matplotlib import pyplot as plt

#2D Convolution ( Image Filtering )
# As in one-dimensional signals, images also can be filtered with various low-pass filters(LPF), 
# high-pass filters(HPF) etc. LPF helps in removing noises, blurring the images etc. HPF filters 
# helps in finding edges in the images.
def two_d_convol():
	img = cv2.imread('opencv_logo.png')
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()


#Image Blurring (Image Smoothing)
# convolving the image with a low-pass filter kernel
# removes high frequency content (eg: noise, edges) from the image

#box filter: averaging
def image_bluring_box():
	img = cv2.imread('opencv-logo-white.png')
	
	blur = cv2.blur(img,(5,5))

	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
	plt.xticks([]), plt.yticks([])
	plt.show()
#gaussian filter: gaussian kernel
# highly effective in removing gaussian noise from the image.
def image_bluring_gaussian():
	img = cv2.imread('opencv-logo-white.png')

	blur = cv2.GaussianBlur(img,(5,5),0) # 0 means both x,y stddevs are calculated from kernel size
	
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
	plt.xticks([]), plt.yticks([])
	plt.show()

#Median Blurring
#  highly effective against salt-and-pepper noise in the images
def image_bluring_median():
	img = cv2.imread('opencv-logo-white-noisy.png')

	blur = cv2.medianBlur(img,11)
	
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
	plt.xticks([]), plt.yticks([])
	plt.show()

#Bilateral Filtering
# smooth while keep edge sharp. Takes 2 gaussian filers.
# Gaussian function of space make sure only nearby pixels are considered for blurring 
# while gaussian function of intensity difference make sure only those pixels with similar 
# intensity to central pixel is considered for blurring.
def image_bluring_bilateral():
	img = cv2.imread('rubberwhale1.png')

	#blur = cv2.medianBlur(img,11)
	blur = cv2.bilateralFilter(img,9,75,75)

	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
	plt.xticks([]), plt.yticks([])
	plt.show()

if __name__ == '__main__':
	#two_d_convol()
	#image_bluring_average()
	#image_bluring_gaussian()
	#image_bluring_median()
	image_bluring_bilateral()