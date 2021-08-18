import cv2
import mediapipe as mp
from mediapipe.python.solutions import drawing_styles
from mediapipe.python.solutions import drawing_utils
from mediapipe.python.solutions import face_mesh

print ("Configure mediapipe...")
mp_face_mesh = face_mesh
mp_drawing = drawing_utils
faces = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5
)
drawing_spec = mp_drawing.DrawingSpec(
    thickness=1,
    circle_radius=1,
    color=(255, 255, 0)
)
camera_id = 1
print (f"Openning camera with device: {camera_id}")
camera = cv2.VideoCapture(camera_id)

running = True
while running:
    ret, frame = camera.read()
    process = faces.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if process.multi_face_landmarks:
        for face_landmarks in process.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACE_CONNECTIONS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec
            )
    
    cv2.imshow("Video", frame)
    
    keys = cv2.waitKey(1) & 0xFF
    if keys == ord("q") or keys == ord("Q"):
        camera.release()
        running = False

cv2.destroyAllWindows()