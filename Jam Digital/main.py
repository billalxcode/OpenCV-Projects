import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def fixTime(text):
    if isinstance(text, int):
        text = str(text)
    
    if isinstance(text, str):
        length = len(text)
        if int(length) == 1:
            text = "0" + text
        return text

def getTime():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    hour = fixTime(hour)
    minute = fixTime(minute)
    second = fixTime(second)
    date = f"{hour}:{minute}:{second}"
    return date

def main():
    print ("Create image...")
    print ("Read font")
    fonts = ImageFont.truetype("digital-7.ttf", 100)
    centerX = int(620 / 2 - 165)
    centerY = int(460 / 2 - 20)

    while True:
        image = Image.new("RGB", (620, 460), (0, 0, 0))
        text = getTime()
        imageDraw = ImageDraw.Draw(image)
        imageDraw.text((centerX, centerY), text, fill=(255, 255, 0), font=fonts)
        print ("Convert with numpy")
        cv_image = np.array(image)
        cv_image = cv_image[:, :, ::-1].copy()
        print ("Convert rgb to bgr")
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
        print ("Show...")
        cv2.imshow("Image", cv_image)

        keys = cv2.waitKey(1) & 0xFF
        if keys == ord("q"):
            cv2.destroyAllWindows()
            break

main()