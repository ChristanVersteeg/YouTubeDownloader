import pyautogui as auto
import keyboard as key

auto.PAUSE = 0.1
X = [137, 309, 489, 647, 112, 291, 496, 681]
Y = [136, 147, 143, 144, 342, 342, 342, 347]
W = 30 #Watering can position

#def print_mouse_position(event):
#    if event.name == 's': print(auto.position())
#key.on_press(print_mouse_position)

def water_plants(event):
    if (event.name == 'w'):
        for i in range(8):
            auto.click(W, W)
            auto.click(X[i], Y[i])
key.on_press(water_plants)

while(True): None