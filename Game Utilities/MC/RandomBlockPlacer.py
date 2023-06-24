from random import choices
import pyautogui
from pynput.mouse import Listener, Button
import keyboard
import Interface; interface = Interface.Interface() 

numbers = list(range(10))  

paused = False

def on_key_press(event):
    global paused
    if event.name == '=':
        paused = not paused
keyboard.on_press(on_key_press)

def on_mouse_click(x, y, button, pressed):
    if button == Button.right and not paused:
        if pressed:
            random_number = choices(numbers, interface.cells)[0]
            pyautogui.press(str(random_number))
     
with Listener(on_click=on_mouse_click) as listener:
    listener.join()