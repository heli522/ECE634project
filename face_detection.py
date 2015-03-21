import cv2

def main():
	cap = cv2.VideoCapture(0)
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	while True:
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		face = None
		for (x, y, w, h) in faces:
			face = cv2. rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			#eyes = eye_cascade.detectMultiScale(roi_gray)
			#for (ex,ey,ew,eh) in eyes:
				#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
			cv2.imshow('face', face)
		cv2.imshow('frame', frame)
		
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break


if __name__ == '__main__':
	main()