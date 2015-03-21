import cv2
import numpy as np

def build_filter():
	Gaborfilters = []
	ksize = 39
	f_max = 0.25
	gamma = 0.5
	psi = 0
	sigma = 0.5
	constant = np.sqrt(2)
	for g in np.arange(0,8,1):
		for theta in np.arange(0,np.pi,np.pi/8):
			lambd = np.power(constant,g)/f_max
			#print lambd
			params = {'ksize':(ksize, ksize), 'sigma':sigma, 'theta':theta, 'lambd':lambd,
			 'gamma':gamma, 'psi':psi, 'ktype':cv2.CV_32F}
			gabor_filter = cv2.getGaborKernel(**params)
            #gabor_filter /=1.0*gabor_filter.sum()

			Gaborfilters.append((gabor_filter,params))
	
	return Gaborfilters


def main(): 
	Gaborfilters = build_filter()
	cap = cv2.VideoCapture(0)

	while True:
		ret, frame = cap.read()
		#break
		width = frame.shape[0]/4
		height = frame.shape[1]/4
		
		feature_vector = []
		grad = np.zeros((width,height),dtype = np.uint8)
		for gabor_filter,params in Gaborfilters:
			gray_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
			#print gray_frame.shapelower_reso_frame = cv2.pyrDown(gray_frame)
			lower_reso_frame = cv2.pyrDown(cv2.pyrDown(gray_frame))
	
			print lower_reso_frame.shape
			#feature_vector.append()
			grad += cv2.filter2D(lower_reso_frame,-1,gabor_filter)
			#break
		#print grad
		cv2.imshow('frame', frame)
		cv2.imshow('gabor',grad)
		cv2.imshow('lower_reso_frame',lower_reso_frame)
		#break

		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
if __name__ == '__main__':
	main()