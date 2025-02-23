import pyautogui
import cv2
import numpy as np
import time
import keyboard


# Constants
x_coord = 606
y_start, y_end = 320, 735
black_threshold = 10
fps = 60
latime = 86

pyautogui.PAUSE = 0  # Removes built-in delay




keyboard.wait("s")
running = True
while running:
    if keyboard.is_pressed("q"):
        print("Emergency stop triggered. ")
        keyboard.wait("s")

    screenshot = pyautogui.screenshot()
    image = np.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


    for i in range(4):
        line = image[y_start:y_end, x_coord+latime*i]
        for y_offset in range(len(line) - 1, -1, -1): 
            pixel = line[y_offset]
            if np.all(pixel < black_threshold):  
                real_y = y_start + y_offset
                pyautogui.moveTo(x_coord+latime*i, real_y-70)
                pyautogui.mouseDown()
                time.sleep(0.01) 
                pyautogui.mouseUp()
                print(f"Clicked at ({x_coord+latime*i}, {real_y-70})")
                break


