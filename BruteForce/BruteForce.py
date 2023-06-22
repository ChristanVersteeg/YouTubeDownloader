import os
import itertools
import pyautogui as auto; auto.PAUSE = 0.1
import keyboard
import json

run = True
progress = {"password_length": 1, "combination_index": 0}
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_ "
MIN_LENGTH = 4
MAX_LENGTH = 12

PROGRESS_FILE = os.path.join(os.environ['LOCALAPPDATA'], 'BruteForce', 'progress.json')
if not os.path.exists(os.path.dirname(PROGRESS_FILE)): os.makedirs(os.path.dirname(PROGRESS_FILE))
if not os.path.exists(PROGRESS_FILE): open(PROGRESS_FILE, 'w')
else: progress = json.load(open(PROGRESS_FILE, 'r'))

password_length = max(progress["password_length"], MIN_LENGTH)
combination_index = progress["combination_index"]

def save_progress(password_length, combination_index):
    progress["password_length"] = password_length
    progress["combination_index"] = combination_index
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

keyboard.wait('backspace')

def exit(_):
    global run
    run = False 
keyboard.on_press_key('s', exit)

for i in range(password_length, MAX_LENGTH + 1):

    combinations = itertools.product(CHARS, repeat=i)

    for j, combination in enumerate(combinations):
        if i == password_length and j < combination_index:
            continue
        
        password = ''.join(combination)
        auto.press('backspace', i + 1)
        auto.write(password)
        auto.press('enter')
        
        if j % 25 == 0: save_progress(i, j)
        
        if not run: 
            save_progress(i, j)
            break
    if not run: break