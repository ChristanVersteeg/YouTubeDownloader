import json
import os
import sys
import keyboard
import time

put = 'input: '
config = {}
config_file = os.path.join(sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(os.path.abspath(__file__)), 'config.json')
config_empty = os.stat(config_file).st_size == 0

def wipe_config(_):
    open(config_file, 'w')
    print("Config wiped!")
keyboard.on_press_key('esc', wipe_config)
    
if(config_empty):
    config[put] = input(put)
    with open(config_file, 'w') as f:
        json.dump(config, f)
        print("Saved!")
else:
    with open(config_file, 'r') as f:
        config = json.load(f)
        print("Loaded!")
print(json.dumps(config))
        
for i in range(30):
    time.sleep(0.1)