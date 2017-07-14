#http://docs.opencv.org/3.2.0/d2/df0/tutorial_py_hdr.html

import cv2
import numpy as np

def Test():
	#################################
	#### Exposure_sequence_HDR() ####
	#################################
	# Loading exposure images into a list
	img_fn = ["img0.jpg", "img1.jpg", "img2.jpg", "img3.jpg"]
	img_list = [cv2.imread(fn) for fn in img_fn]
	exposure_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)

	# Merge exposures to HDR image
	merge_debvec = cv2.createMergeDebevec()
	hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy())
	merge_robertson = cv2.createMergeRobertson()
	hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy())

	# Tonemap HDR image
	tonemap1 = cv2.createTonemapDurand(gamma=2.2)
	res_debvec = tonemap1.process(hdr_debvec.copy())
	tonemap2 = cv2.createTonemapDurand(gamma=1.3)
	res_robertson = tonemap2.process(hdr_robertson.copy())

	# Exposure fusion using Mertens (don't need exposure time and tone mapping, it already give result in [0,1])
	merge_mertens = cv2.createMergeMertens()
	res_mertens = merge_mertens.process(img_list)

	# Convert datatype to 8-bit and save
	res_debvec_8bit = np.clip(res_debvec*255, 0, 255).astype('uint8')
	res_robertson_8bit = np.clip(res_robertson*255, 0, 255).astype('uint8')
	res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
	cv2.imwrite("ldr_debvec.jpg", res_debvec_8bit)
	cv2.imwrite("ldr_robertson.jpg", res_robertson_8bit)
	cv2.imwrite("fusion_mertens.jpg", res_mertens_8bit)


	#################################################
	#### Estimate camera response function (CRF) ####
	#################################################
	#The camera response function (CRF) gives us the 
	#connection between the scene radiance to the measured intensity values. 
	cal_debvec = cv2.createCalibrateDebevec()
	crf_debvec = cal_debvec.process(img_list, times=exposure_times)
	hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy(), response=crf_debvec.copy())
	cal_robertson = cv2.createCalibrateRobertson()
	crf_robertson = cal_robertson.process(img_list, times=exposure_times)
	hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy(), response=crf_robertson.copy())	

#robertson is similar to Debevec
def HDRDebevec(img_fn, exposure_times, if_crf=False):
	img_list = [cv2.imread(fn) for fn in img_fn]
	if if_crf :
		merge_debvec = cv2.createMergeDebevec()
		cal_debvec = cv2.createCalibrateDebevec()
		crf_debvec = cal_debvec.process(img_list, times=exposure_times)
		hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy(), response=crf_debvec.copy())
	else:
		merge_debvec = cv2.createMergeDebevec()
		hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy())

	tonemap1 = cv2.createTonemapDurand(gamma=2.2)
	res_debvec = tonemap1.process(hdr_debvec.copy())

	res_debvec_8bit = np.clip(res_debvec*255, 0, 255).astype('uint8')
	cv2.imwrite("ldr_debvec_0.jpg", res_debvec_8bit)

def HDRMertens(img_fn, exposure_times):
	img_list = [cv2.imread(fn) for fn in img_fn]
	merge_mertens = cv2.createMergeMertens()
	res_mertens = merge_mertens.process(img_list)
	res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
	cv2.imwrite("fusion_mertens_0.jpg", res_mertens_8bit)


if __name__ == '__main__':
	img_fn = ["img0.jpg", "img1.jpg", "img2.jpg", "img3.jpg"]
	exposure_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)
	HDRDebevec(img_fn, exposure_times, False)
	HDRMertens(img_fn, exposure_times)