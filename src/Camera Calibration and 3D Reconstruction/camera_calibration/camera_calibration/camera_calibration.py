#http://docs.opencv.org/3.2.0/dc/dbb/tutorial_py_calibration.html
import numpy as np
import cv2
import glob

def SetUp():
	# termination criteria
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
	# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
	objp = np.zeros((6*7,3), np.float32)
	objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
	# Arrays to store object points and image points from all the images.
	objpoints = [] # 3d point in real world space
	imgpoints = [] # 2d points in image plane.
	images = glob.glob('*.jpg')
	for fname in images:
		img = cv2.imread(fname)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# Find the chess board corners
		ret, corners = cv2.findChessboardCorners(gray, (7,6), None)
		# If found, add object points, image points (after refining them)
		if ret == True:
			objpoints.append(objp)
			corners2=cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
			imgpoints.append(corners)
			# Draw and display the corners
			cv2.drawChessboardCorners(img, (7,6), corners2, ret)
			cv2.imshow('img', img)
			cv2.waitKey(100)
	cv2.destroyAllWindows()
	return objpoints, imgpoints, gray

#camera matrix, distortion coefficients, rotation and translation vectors 
def Calibration(objpoints, imgpoints, gray):
	ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
	return ret, mtx, dist, rvecs, tvecs

def Undistortion(mtx, dist):
	img = cv2.imread('left12.jpg')
	h,  w = img.shape[:2]
	newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
	option = True
	if option:
		#1.0 cv2.undistort
		# undistort
		dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
		# crop the image
		x, y, w, h = roi
		dst = dst[y:y+h, x:x+w]
		cv2.imwrite('calibresult.png', dst)
	else:
		#2.0 Using remapping
		# undistort
		mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
		dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
		# crop the image
		x, y, w, h = roi
		dst = dst[y:y+h, x:x+w]
		cv2.imwrite('calibresult.png', dst)

# store the camera matrix and distortion coefficients using write functions in Numpy (np.savez, np.savetxt etc) 
def	 StoreCalibrationRet(mtx, dist, rvecs, tvecs):
	np.savez("calibration.npz", mtx = mtx, dist = dist, rvecs = rvecs, tvecs = tvecs)
	#r = np.load("calibration.npz")
	#print r["mtx"], r["dist"],  r["rvecs"], r["tvecs"]
	pass

def Re_projection_Error(objpoints,imgpoints, rvecs, tvecs, mtx, dist):
	mean_error = 0
	for i in xrange(len(objpoints)):
		imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
		error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
		mean_error += error
	print "total error: ", mean_error/len(objpoints)

if __name__ == '__main__':
	 objpoints, imgpoints, gray = SetUp()
	 ret, mtx, dist, rvecs, tvecs = Calibration(objpoints, imgpoints, gray)
	 Undistortion(mtx, dist)
	 StoreCalibrationRet(mtx, dist, rvecs, tvecs)
	 Re_projection_Error(objpoints,imgpoints, rvecs, tvecs, mtx, dist)