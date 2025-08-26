import pytesseract
import cv2
from PIL import Image
import os
import pyttsx3
from picamera2 import Picamera2
 
language = 'en'
engine = pyttsx3.init()
engine.setProperty('rate', 100) 
piCam = Picamera2()
piCam.preview_configuration.main.size=(800,600)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.align()
# piCam.configure("preview")
piCam.start()
key = cv2. waitKey(1)
 
while True:
    try:
        frame = piCam.capture_array()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('z'):
            print("Saving Frame");
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            string = pytesseract.image_to_string(frame)
            print(string)
            engine.setProperty('rate', 125) 
            engine.say("hi")
            engine.say(string)
            engine.runAndWait()
            print("Image saved!")
            break
 
 
    except(KeyboardInterrupt):
        print("Turning off camera.")
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break;
 
