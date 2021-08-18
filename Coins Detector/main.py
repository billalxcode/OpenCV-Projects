import cv2
import numpy as np

id = 0
camera = cv2.VideoCapture(id)
while True:
    ret, frame = camera.read()

    blur = cv2.GaussianBlur(frame, (11, 11), 0)
    edges = cv2.Canny(blur, 40, 150)
    dilated = cv2.dilate(edges, (1, 1), iterations=2)
    (cnt, _) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print ("Terdapat: " + str(len(cnt)))
    for countours in cnt:
        (x, y, w, h) = cv2.boundingRect(countours)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    cv2.imshow("frame", frame)

    keys = cv2.waitKey(1) & 0xFF
    if keys == ord("Q") or keys == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        break