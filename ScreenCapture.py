import win32gui
import numpy as np
import cv2
import pyautogui as auto

def get_screenshot():
    # Get handle of the current top-most window
    hwnd = win32gui.GetForegroundWindow()

    # Get coordinates of the window
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    # Get the screenshot
    screenshot = np.array(auto.screenshot())
    
    # Crop the screenshot to the size of the window
    screenshot = screenshot[top:bottom, left:right]

    return screenshot

# Example usage:
screenshot = cv2.cvtColor(get_screenshot(), cv2.COLOR_BGR2GRAY)
cv2.imshow('screenshot', screenshot)
cv2.waitKey(0)