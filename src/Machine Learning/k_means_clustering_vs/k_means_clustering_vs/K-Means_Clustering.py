#http://docs.opencv.org/3.2.0/d9/d70/tutorial_py_kmeans_index.html
#http://www.csdn.net/article/2012-07-03/2807073-k-means

import numpy as np
import cv2
from matplotlib import pyplot as plt

def DataWithOneFeature():
	x = np.random.randint(25,100,25)
	y = np.random.randint(175,255,25)
	z = np.hstack((x,y))
	z = z.reshape((50,1))
	z = np.float32(z)
	plt.hist(z,256,[0,256]),plt.show()

	# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	# Set flags (Just to avoid line break in the code)
	flags = cv2.KMEANS_RANDOM_CENTERS
	# Apply KMeans
	compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)

	A = z[labels==0]
	B = z[labels==1]

	# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
	plt.hist(A,256,[0,256],color = 'r')
	plt.hist(B,256,[0,256],color = 'b')
	plt.hist(centers,32,[0,256],color = 'y')
	plt.show()


def DataWithMultipleFeature():
	X = np.random.randint(25,50,(25,2))
	Y = np.random.randint(60,85,(25,2))
	Z = np.vstack((X,Y))
	# convert to np.float32
	Z = np.float32(Z)
	# define criteria and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret, label, center = cv2.kmeans(Z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	# Now separate the data, Note the flatten()
	A = Z[label.ravel()==0]
	B = Z[label.ravel()==1]
	# Plot the data
	plt.scatter(A[:,0], A[:,1])
	plt.scatter(B[:,0], B[:,1], c = 'r')
	plt.scatter(center[:,0], center[:,1],s = 80,c = 'y', marker = 's')
	plt.xlabel('Height'),plt.ylabel('Weight')
	plt.show()

#treate img's pixels as samples with 3 features(r,g,b); then clustering them based on the 3 features using KNN; 
#set all samples's feature value to the center feature value of their corresponding cluster 
def Color_Quantization():
	img = cv2.imread('messi5.jpg')
	Z = img.reshape((-1,3)) # convert to 3 coloums (r,g,b)
	# convert uint8 to np.float32
	Z = np.float32(Z)
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	K = 8
	ret, label, center = cv2.kmeans( Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	# Now convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	cv2.imshow('res2',res2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	# DataWithOneFeature()
	#DataWithMultipleFeature()
	Color_Quantization()