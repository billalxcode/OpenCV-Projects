import cv2
from time import time
from threading import Thread

camera_id = 1 # Change it
camera = cv2.VideoCapture(camera_id)
counter = 0

if camera.isOpened() is False:
    print ("Cannot open camera!")
    exit(0)

def startCamera(camera):
    global counter
    pTime = 0
    while True:
        ret, frame = camera.read()

        filename = f"output/output-camera-frame-{counter}.jpg"
        cv2.imwrite(filename, frame)
        # FPS
        current_time = time()
        fps = 1/(current_time-pTime)
        pTime = current_time
        print (f"\r[{counter}] Save file into: {filename} with fps: {round(fps)}", end="")
        cv2.putText(frame, f"FPS: {round(fps)}", (10, 25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 255), 2)
        cv2.imshow("Camera", frame)
        counter += 1
        keys = cv2.waitKey(1) & 0xFF
        if keys == ord("q") or keys == ord("Q"):
            camera.release()
            break

th = Thread(target=startCamera, args=(camera,))
th.start()
cv2.destroyAllWindows()