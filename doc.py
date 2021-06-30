from PIL import ImageGrab
import numpy as np
import cv2


while True:
    img = ImageGrab.grab(bbox=(0, 0, 1280, 720))
    img_np = np.array(img)
    cv2.imshow('Secret Capture', img_np)
    cv2.waitKey(10)
