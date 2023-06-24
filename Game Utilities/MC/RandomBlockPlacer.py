from random import choices
import pyautogui
from pynput.mouse import Listener, Button
import keyboard
from threading import Thread
from Interface import Interface

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
            cell_values = [int(cell.get()) for cell in interface.cells if cell.get()]
            if cell_values:
                random_number = choices(numbers, k=1)[0]
                pyautogui.press(str(random_number))

interface = Interface()

listener_thread = Thread(target=Listener(on_click=on_mouse_click).start)
listener_thread.start()

interface.run()
