#You need to install IP Webcam or DroidCam application in your Andriod or Any Devices
#It requires Internet
import cv2
import numpy as np 
print("For Example: \n\thttps://123.43.203.19:5680/video \n http://123.43.203.19:2350/video \n rtsp://123.32.256.8:8080/video")
url=input("\nEnter URL of IP Webcam Here: ")
cp=cv2.VideoCapture(url)
while True:
	camera,frame=cp.read()
	if frame is not None:
		cv2.imshow("Frame",frame)
#Press q to exit the loop and exits automatically
	q=cv2.waitKey(1)
	if q==ord("q"):
		break
cv2.destroyAllWindows()

