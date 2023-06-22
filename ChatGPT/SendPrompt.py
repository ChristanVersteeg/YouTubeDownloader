import sys
import os
import cv2
import numpy as np
import pyautogui as auto
import keyboard

running = True
def quit(_): global running; running = False
keyboard.on_press_key('esc', quit)

auto.PAUSE = 0.01
screenshot = None
loc1_offset = (25, 25)
threshold = 0.8
def path(name): return os.path.join(sys._MEIPASS, f'{name}.png')
def load(image): return cv2.imread(image, cv2.IMREAD_GRAYSCALE)
send_button = load(path('send_button'))
save_and_submit_button = load(path('save_and_submit_button'))

def image_found(loc): return len(loc[0]) > 0 and len(loc[1]) > 0

def locate_image(image): 
    loc = np.where(cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED) >= threshold)
    
    return loc

def find_image(_):
    if keyboard.is_pressed('shift+enter'): return
    if not keyboard.is_pressed('enter'): return
    
    global screenshot
    screenshot = cv2.cvtColor(np.array(auto.screenshot()), cv2.COLOR_BGR2GRAY)
    
    loc = locate_image(send_button)
    if not image_found(loc): return

    loc1 = locate_image(save_and_submit_button)
    loc = np.add(loc1, loc1_offset) if image_found(loc1) else loc
    
    auto.press('backspace')
    
    auto.click(loc[1][0], loc[0][0])
    
    auto.hotkey('shift', 'tab')
keyboard.on_press(find_image)

while running: pass