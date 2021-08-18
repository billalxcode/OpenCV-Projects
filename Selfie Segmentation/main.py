import cv2
import mediapipe as mp
import numpy as np
from mediapipe.python.solutions import drawing_styles
from mediapipe.python.solutions import drawing_utils
from mediapipe.python.solutions import selfie_segmentation

mp_drawing = drawing_utils
mp_selfie_segmentations = selfie_segmentation
selfie = selfie_segmentation.SelfieSegmentation(
    model_selection=0
)

camera_id = 0
camera = cv2.VideoCapture(camera_id)

running = True
while running:
    ret, frame = camera.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    process = selfie.process(frame_rgb)

    condition = np.stack((process.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(frame.shape, dtype=np.uint8)
    bg_image[:] = (255, 255, 255)

    frame = np.where(condition, frame, bg_image)
    cv2.imshow("Video", frame)

    keys = cv2.waitKey(1) & 0xFF

    if keys == ord("Q") or keys == ord("q"):
        camera.release()
        running = False

cv2.destroyAllWindows()