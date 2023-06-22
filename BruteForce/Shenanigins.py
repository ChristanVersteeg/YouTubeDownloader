import pyautogui; pyautogui.PAUSE = 0.3
from time import sleep
#sleep(5)
#x, y = pyautogui.position()
#print(f"Current mouse position: ({x}, {y})")

x = 500
y = 177
name = "DiscordUserName"
tag = 1000
counter_max = 10000

sleep(3)
pyautogui.click(x, y)  
pyautogui.write(name)
while tag < counter_max:  
    pyautogui.typewrite(str(tag)) 
    
    pyautogui.press('enter')
    pyautogui.press('enter')
    
    sleep(0.3)
    
    pyautogui.click(x, y)  
    
    pyautogui.press('backspace', 4)   

    tag += 1 