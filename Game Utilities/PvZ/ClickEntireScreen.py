import pyautogui as auto
import keyboard as key

auto.PAUSE = 0.01
toggle = False
PIXEL_JUMP = 50 
OFFSET = 25 
 
def toggle_p(event):
    global toggle
    if event.name == 'p':
        toggle = not toggle
key.on_press(toggle_p)

while(True):
    if(toggle):
        for y in range(1, 10):
            if not toggle: break
            for x in range(1, 16):
                auto.click(x=PIXEL_JUMP*x, y=PIXEL_JUMP*y + OFFSET)
                if not toggle: break