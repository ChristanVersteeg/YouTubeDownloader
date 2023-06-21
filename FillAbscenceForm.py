from datetime import datetime
import pyautogui as auto; auto.PAUSE = 0.1
import os
import json
from keyboard import on_press_key
import re
import sys
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d = datetime.now()
class Field(Enum):
    DATE = f'{d.day}-{d.month}-{d.year}'
    CHILD_NAME = 'child_name'
    CLASS = 'class'
    PARENT_NAME = 'parent_name'
    PHONE_NUMBER = 'phone_number'
    EMAIL = 'email'
    
config = {}
config_file = os.path.join(os.environ['LOCALAPPDATA'], 'FillAbsenceForm', 'config.json')
if not os.path.exists(os.path.dirname(config_file)): os.makedirs(os.path.dirname(config_file))
if not os.path.exists(config_file): open(config_file, 'w')
config_empty = os.stat(config_file).st_size == 0
valid_number =  r'^(\s?\d\s?){7}\s?\d$'
valid_email = r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
user_input = ""
running = True
default_input_error = 'Ongeldige invoer'
timeout_delay = 5
exception_string = 'Telefoonnummer: (06)'

def check_running(func):
    def wrapper(*args, **kwargs):
        global running
        if running:
            func(*args, **kwargs)
        else:
            return
    return wrapper

def invalid_input(description = exception_string):
    global user_input
    user_input = input(f"   {description}: ") if description != exception_string else input(f"   {description}")
    return len(user_input) == 0
    
def add_config_value(field, description = exception_string):
    global config
    while invalid_input(description):
        print(default_input_error)
    config[field.value] = user_input
    return user_input

def wipe_config(_):
    global running
    open(config_file, 'w')
    running = False
on_press_key('esc', wipe_config)

if config_empty:
    print("--------Copyright Christan Versteeg 2023-------")
    print("(https://www.linkedin.com/in/christan-versteeg)")
    print("-----------------------------------------------")
    
    print("\nConfigureer uw gegevens:")
    add_config_value(Field.CHILD_NAME, 'Voor- en achternaam leerling')
    add_config_value(Field.CLASS, 'Klas')
    add_config_value(Field.PARENT_NAME, 'Uw naam')

    while(not re.match(valid_number, add_config_value(Field.PHONE_NUMBER))):
        print("Ongeldig telefoonnummer.")
    config[Field.PHONE_NUMBER.value] = "06" + config[Field.PHONE_NUMBER.value]

    while(not re.match(valid_email, add_config_value(Field.EMAIL, 'E-mailadres'))):
        print("Ongeldig e-mailadres.")
        
    print("\nConfiguratie voltooid. Indien nodig, kunt u de configuratie verwijderen door tijdens het uitvoeren van het programma op de \"ESC\"-knop te drukken.")
    
    with open(config_file, 'w') as f:
        json.dump(config, f)
    
    def execution_prompt():
        global user_input
        user_input = input('\nWilt u het programma direct uitvoeren? J/N: ').lower()
        return user_input != 'n' and user_input != 'j'

    while execution_prompt():
        print(default_input_error)

    if user_input == 'n': sys.exit()
        
else:
    with open(config_file, 'r') as f:
        config = json.load(f)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--new-tab")
chrome_options.add_argument("--window-size=500,1000")
chrome_options.add_argument("--window-position=0,0")
chrome_options.add_argument("--disable-extensions")
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://fd8.formdesk.com/montessorilyceumamsterdam/verzuim-versie-maart2017")

def fill_field(field, presses=1):
    auto.write(config[field.value]) if field != Field.DATE else auto.write(field.value)
    auto.press('tab', presses)

def set_default_absence_time():
    auto.press('tab', 8)
    auto.press('space')
    auto.press('tab')
     
def set_default_abscence_reason():
    auto.press('enter')
    auto.press('down', 2)
    auto.press('enter')
    auto.press('tab', 2)

def fill_form():
    WebDriverWait(chrome, timeout_delay).until(EC.element_to_be_clickable((By.ID, "datum_van_verzuima_"))).click()
    fill_field(Field.DATE, 2)
    fill_field(Field.CHILD_NAME)
    fill_field(Field.CLASS)
    set_default_absence_time()
    set_default_abscence_reason()
    fill_field(Field.PARENT_NAME)
    fill_field(Field.PHONE_NUMBER)
    fill_field(Field.EMAIL)
    
for func_name in [fill_field, set_default_absence_time, set_default_abscence_reason, fill_form]:
    locals()[func_name.__name__] = check_running(func_name)
    
fill_form()

while running:
    try:
        chrome.title
    except:
        break
chrome.quit()
sys.exit()