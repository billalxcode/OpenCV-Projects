import cv2
import numpy as np
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import IntVar

class Capture:
    def __init__(self, id=0):
        self.camera = cv2.VideoCapture(id)
        self.settings()
        self.frame = np.array([])
        self.count += 1

    def settings(self):
        self.cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")

    def detect(self, id, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(
            gray,
            1.35,
            5
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
            self.save(id)
            self.count += 1

    def save(self, id):
        pass

    def read(self):
        ret, frame = self.camera.read()
        return ret, frame

class GUI:
    def __init__(self) -> None:
        self.camera = Capture()
        self.root = Tk()
        self.EIDValue = IntVar()
        self.frame = Frame(self.root)
        self.frame.grid(column=0, row=0, pady=10, padx=10)
        self.datasetID_entry = None
        self.isRun = False

    def update(self):
        self.capture_btn.config(text=("Process" if self.isRun else "Capture"))
        
    def process(self):
        self.isRun = (False if self.isRun else True)
        self.update()
        while self.isRun:
            ret, frame = self.camera.read()

    def settings(self):
        # settings window
        self.root.title("Capture Face")
        self.root.geometry("400x200")

        # Settings UI
        self.datasetID_label = Label(self.frame, text="Dataset ID: ")
        self.datasetID_label.grid(column=0, row=0)
        self.datasetID_entry = Entry(self.frame, textvariable=self.EIDValue)
        self.datasetID_entry.grid(column=1, row=0)
        self.capture_btn = Button(self.root, text="Capture", command=self.process)
        self.capture_btn.grid(column=0, row=1, pady=10, padx=50)

    def main(self):
        self.settings()
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.main()