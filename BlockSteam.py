import pyautogui as auto
from random import randint

class Key:
    BACKSPACE = 'backspace'
    TAB = 'tab'
    ENTER = 'enter'
    
auto.PAUSE = 0.01
pin_length = 4
field_count = 2

def get_pin():
    pin = ""
    for _ in range(pin_length):
        pin += f"{randint(0, 9)}"
    return pin

def write_pin(pin):
    auto.press(Key.BACKSPACE)
    for _ in range(field_count):
        auto.typewrite(pin)
        auto.press(Key.TAB)
    auto.press(Key.ENTER)

write_pin(get_pin())