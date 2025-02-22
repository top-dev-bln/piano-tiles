import pyautogui
import cv2
import numpy as np
region_screenshot = pyautogui.screenshot(region=(564, 182, 342, 606))
full = pyautogui.screenshot()
full.save("screenshot.png")
image = np.array(region_screenshot)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

line1 = reversed(gray_image[42,0:606])

for y, pixel in enumerate(line1):
    if pixel == 0:  # Black pixel check
        print(f"Black pixel found at: ({606}, {y + 129-80})")
        

cv2.imwrite("grayscale_screenshot.png", gray_image)
