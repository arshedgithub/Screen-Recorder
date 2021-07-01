from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics, Sleep
import datetime
import pyttsx3


speaker = pyttsx3.init()
speaker.say("Recording will start in 10 seconds")
speaker.runAndWait()

print('starting...')
print("'s' for open web cam\n'f' for close webcam\n'q' for stop recording")
speaker.say("press, 's' on keyboard to web cam on, and press. 'f' to off the cam")
speaker.runAndWait()

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
file_name = f'sr{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(0)
webcam_open = False


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()

    if cv2.waitKey(10) == ord('s'):
        webcam_open = True
    elif cv2.waitKey(10) == ord('f'):
        webcam_open = False
    elif cv2.waitKey(10) == ord('q'):
        break

    if webcam_open == True:
        fr_height, fr_width, _ = frame.shape
        img_final[0:fr_height, 0: fr_width,
                  :] = frame[0:fr_height, 0: fr_width, :]

    cv2.imshow("Ninja's Screen Recorder", img_final)
    # cv2.imshow("Ninja's Web Cam", frame)
    captured_video.write(img_final)
