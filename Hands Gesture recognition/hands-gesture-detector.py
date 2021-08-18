import cv2
import time
import mediapipe as mp
from mediapipe.python.solutions import drawing_styles, drawing_utils
from mediapipe.python.solutions import hands
running = True
camera_width = 640
camera_height = 640
angka = ""
target_landmark = [4, 8, 12, 16, 20]

camera = cv2.VideoCapture(0)
camera.set(3, camera_width)
camera.set(4, camera_height)

mp_drawing = drawing_utils
mp_hands = hands
drawing_style = drawing_styles
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)

pTime = 0
while running:
    landmark_lists = []

    ret, frame = camera.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect fps
    current_time = time.time()
    fps = 1/(current_time-pTime)
    pTime = current_time

    # Detect hands
    process = hands.process(rgb_frame)
    if process.multi_hand_landmarks:
        for hand_landmarks in process.multi_hand_landmarks:
            hand_landmark = process.multi_hand_landmarks[0]
            for id, lm in enumerate(hand_landmark.landmark):
                h, w, c = frame.shape
                x, y = int(lm.x * w), int(lm.y * h)
                landmark_lists.append([id, x, y])
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                # drawing_style.get_default_hand_landmark_style(),
                # drawing_style.get_default_hand_connection_style()
            )

    if len(landmark_lists) != 0:
        fingers = []

        if landmark_lists[target_landmark[0]][1] > landmark_lists[target_landmark[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        for ids in range(1, 5):
            if landmark_lists[target_landmark[ids]][2] < landmark_lists[target_landmark[ids]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        angka = str(fingers.count(1))
        print (fingers)
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f"Angka: {angka}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Camera", frame)

    keys = cv2.waitKey(1) & 0xFF
    if keys == ord("q") or keys == ord("Q"):
        camera.release()
        cv2.destroyAllWindows()
        running = False
