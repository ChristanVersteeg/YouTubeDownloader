import pyautogui as auto
from keyboard import on_press

toggle_picking = False
toggle_watering = False
PIXEL_JUMP = 50 
OFFSET = 25
X = [137, 309, 489, 647, 112, 291, 496, 681]
Y = [136, 147, 143, 144, 342, 342, 342, 347]
W = 30
FAST = 0.01
SLOW = 0.1
auto.PAUSE = FAST
 
#def print_mouse_position(event):
#    if event.name == 's': print(auto.position())
#key.on_press(print_mouse_position)

#region TOGGLES
def toggle(event, key, toggle):
    if event.name == key:
        toggle = not toggle
        return toggle

def toggle_p(event):
    global toggle_picking
    toggle_picking = toggle(event, 'p', toggle_picking)
on_press(toggle_p)

def toggle_o(event):
    global toggle_watering
    toggle_watering = toggle(event, 'o', toggle_watering)
on_press(toggle_o)
#endregion

def water_plants(event):
    if (event.name == 'w'):
        while(True):
            auto.PAUSE = SLOW
            for i in range(8):
                auto.click(W, W)
                auto.click(X[i], Y[i])
            auto.PAUSE = FAST
            if not toggle_watering: break
on_press(water_plants)

while(True):
    print(toggle_watering)
    if(toggle_picking):
        for y in range(1, 10):
            if not toggle_picking: break
            for x in range(1, 16):
                auto.click(x=PIXEL_JUMP*x, y=PIXEL_JUMP*y + OFFSET)
                if not toggle_picking: break