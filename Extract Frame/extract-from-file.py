import cv2
from os.path import isfile
from time import time

video_path = "videos.mp4"
if not isfile(video_path):
    print ("File not found")
    exit(0)
video = cv2.VideoCapture(video_path)

counter = 0
start_time = time()
while True:
    ret, frame = video.read()
    if ret is False: break
    filename = f"output/frame-{counter}.jpg"
    cv2.imwrite(filename, frame)
    print (f"\r[{counter}] Save file into: {filename}", end="")
    counter += 1
print (f"\n[!] Done, time: {round(time() - start_time)}s")