from random import choices
import pyautogui
from pynput.mouse import Listener, Button
import keyboard
from threading import Thread
from Interface import Interface

numbers = list(range(1, 10)) + [0]

def on_mouse_click(x, y, button, pressed):
    if button == Button.right and not interface.paused:
        if pressed:
            cell_values = [int(cell.get()) if cell.get().isdigit() else 0 for cell in interface.cells]
            if any(cell_values):
                random_number = choices(numbers, cell_values)[0]
                pyautogui.press(str(random_number))

interface = Interface()

listener_thread = Thread(target=Listener(on_click=on_mouse_click).start)
listener_thread.start()

interface.run()