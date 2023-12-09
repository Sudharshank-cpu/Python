import cv2
#Load Cascade
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#To Capture from WebCam
cap=cv2.VideoCapture(0)
#To use Video file as Input
#cap=cv2.VideoCapture('filename.mp4')
while True:
	#Read Frames
	_,img=cap.read()
	#Convert to Grayscale
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#Detect Faces
	faces=face_cascade.detectMultiScale(gray,1.1,4)
	#Draw Rectangle around Each Face
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	#Display
	cv2.imshow('img',img)
	#Stop if Escape Key is Pressed
	k=cv2.waitKey(30) & 0xff
	if k==27:
		break
#Release Video Capture Object
cap.release()
#"pip install opencv-python" to import cv2(pip version is above 3.4)
