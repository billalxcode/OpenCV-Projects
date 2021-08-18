from cv2 import VideoCapture
from cv2 import imshow
from cv2 import CascadeClassifier
from cv2 import rectangle
from cv2 import waitKey
from cv2 import cvtColor
from cv2 import COLOR_BGR2GRAY
from cv2 import flip
from cv2 import rotate

def main():
    videos = VideoCapture(0)
    cascade = CascadeClassifier("data/haarcascade_frontalface_default.xml")

    while 1:
        ret, frame = videos.read()
        
        frame = rotate(frame, 2)
        gray = cvtColor(frame, COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(
            gray,
        )
        for (x, y, w, h) in faces:
            rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        imshow("Frames", frame)

        keys = waitKey(1)
        if keys & 0xFF == ord("q"):
            break

if __name__ == "__main__":
    main()