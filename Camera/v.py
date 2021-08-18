import cv2

camera = cv2.VideoCapture(0)

while True:
	ret, frame = camera.read()

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("q") or key == ord("Q"):
		camera.release()
		cv2.destroyAllWindows()
		break


