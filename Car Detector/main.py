import cv2

path_image = "images.jpg"
fonts = cv2.FONT_HERSHEY_COMPLEX_SMALL
text_position = (10, 20)

images = cv2.imread(path_image)
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11, 11), 0)
edges = cv2.Canny(blur, 40, 150)
dilate = cv2.dilate(edges, (1, 1), iterations=2)

countours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for countour in countours:
    (x, y, w, h) = cv2.boundingRect(countour)
    cv2.rectangle(images, (x, y), (x+w, y+h), (0, 255, 0), 2)

text = f"Terdapat {len(countours)} object"
cv2.putText(images, text, text_position, fonts, 1, (0, 255, 255), 1)

while True:
    cv2.imshow("Frame", images)

    keys = cv2.waitKey(1) & 0xFF
    if keys == ord("q") or keys == ord("Q"):
        cv2.destroyAllWindows()
        break