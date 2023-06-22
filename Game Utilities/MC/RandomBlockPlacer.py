from random import choices
import pyautogui
from pynput.mouse import Listener, Button
import keyboard

numbers = list(range(10))  
#          0  1  2  3  4  5  6  7  8  9
weights = [0, 10, 10, 5, 1, 0, 0, 0, 0, 0]  

paused = False

def calculate_odds(weights):
    total_weight = sum(weights)
    odds = [weight / total_weight for weight in weights]
    return odds

for choice, odd in enumerate(calculate_odds(weights)):
    print(f"Choice {choice}: {odd:.3f} ({odd * 100:.1f}%)")

def on_key_press(event):
    global paused
    if event.name == '=':
        paused = not paused
keyboard.on_press(on_key_press)

def on_mouse_click(x, y, button, pressed):
    if button == Button.right and not paused:
        if pressed:
            random_number = choices(numbers, weights=weights)[0]
            pyautogui.press(str(random_number))

with Listener(on_click=on_mouse_click) as listener:
    listener.join()