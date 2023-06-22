#Import is not recognised because it's only recognised in OBS itself, not through PIP install or any other means.
import obspython as obs
import json as js
import os

#Variables
script_active = True
json_path = ""
netherite_beacon_ancient_debris_cost = 5904
tools_and_armor_cost = 32 # 4 Ancient Debris * 4 Armor Pieces + 4 Ancient Debris * 4 Tools, This excludes the Netherite Hoe
required_ancient_debris = netherite_beacon_ancient_debris_cost + tools_and_armor_cost

front_ancient_debris = ""
difference_ancient_debris = ""

file_path = os.path.abspath(os.path.dirname(__file__))
refresh_time = 500

#The visible properties that the user can adjust in OBS itself.
def script_properties():

    props = obs.obs_properties_create()

    obs.obs_properties_add_bool(props, "script_active", "Script Active")

    obs.obs_properties_add_path(props, "json_path", "Json Path", obs.OBS_PATH_FILE, "Json (*.json)", '')

    obs.obs_properties_add_text(props, "front_ancient_debris", "Ancient Debris Front Display Text", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "difference_ancient_debris", "Ancient Debris Difference Display Text", obs.OBS_TEXT_DEFAULT)

    return props

#Updates the settings whenever a setting is changed.
def script_update(settings):

    #All variables use the global keyword so it takes the variables from outside this method.
    global script_active 
    script_active = obs.obs_data_get_bool(settings, "script_active")

    global json_path 
    json_path = obs.obs_data_get_string(settings, "json_path")

    global front_ancient_debris 
    global back_ancient_debris 
    global difference_ancient_debris
    front_ancient_debris = obs.obs_data_get_string(settings, "front_ancient_debris")
    difference_ancient_debris = obs.obs_data_get_string(settings, "difference_ancient_debris")

    #Checks if the boolean for the script being activge is true, if it is load the settings, thus enabling the timer and the script,
    #else unload the script and discard the timer thus stopping the script.
    if (script_active):
        script_load(settings)
    else:
        script_unload()

    return True

def run():

    #Checks if the json_path is not empty so it doesn't throw a nullreference.
    if (json_path is not ""): 
        
        #Opens the json file in read mode amnd loads it in a variable, then it gets filtered into another variable
        #For the specific block you're mining, in this case ancient debris.
        with open (json_path, "r") as json:
            stats = js.load(json)
            filtered_stats = stats['stats']['minecraft:mined']["minecraft:ancient_debris"]

        #Opens a .txt document, if it doesn't exist, it'll create one. It writes the filtered stats in the txt and the extra string the user has given, if any.
        with open(f"{file_path}/Statistics.txt", "w+") as txt:
            txt.write(f"{front_ancient_debris}{filtered_stats}/{required_ancient_debris}")
            txt.close()

        with open(f"{file_path}/StatisticsDifference.txt", "w+") as txt:
            txt.write(f"{difference_ancient_debris}{required_ancient_debris-filtered_stats} ({filtered_stats/required_ancient_debris*100:.2f}%)")
            txt.close()

    #A debug print so that if something does go wrong, the console will say so and it won't just stay empty.
    else: print(".json path is empty")

#Upon OBS startup, runs this function, checks if the script is active, if so, it will add the timer with a refresh rate of 500ms.
def script_load(settings):
    if(script_active): obs.timer_add(run, refresh_time)

#Upon closing OBS, it'll run this function, removing the timer if there was one.
def script_unload():
    obs.timer_remove(run)