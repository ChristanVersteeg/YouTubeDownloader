#Made by Christan Versteeg; https://github.com/ChristanVersteeg/python_projects/tree/main/YoutubeDownloader

import os
import re
import shutil
import pytube
from enum import Enum
from moviepy.editor import VideoFileClip, AudioFileClip
import ctypes
VIDEO_URL = """
https://youtu.be/lz156C981fs
"""
YT = pytube.YouTube(VIDEO_URL)

EXTENSION = ".mp4"
TEMP_PATH = "./Temp/"

if not os.path.exists(TEMP_PATH): os.mkdir(TEMP_PATH)
ctypes.windll.kernel32.SetFileAttributesW(TEMP_PATH, 0x2)

#If you want it clean you could use TITLE = fr"{re.sub(r'[^\w\s]', '', YT.title)}{EXTENSION}",
TITLE = re.sub(r'[^\w\s]', '', YT.title) + EXTENSION 
TEMP_TITLE = f"{TEMP_PATH}{TITLE}"
#but that only works in Python 3.12, which is in pre-release.

if os.path.exists(TITLE): os.remove(TITLE)

class Type(Enum):
    VIDEO = f"{TEMP_PATH}video{EXTENSION}"
    AUDIO = f"{TEMP_PATH}audio{EXTENSION}"
    
for type in Type: YT.streams.filter(only_video = type.value == Type.VIDEO.value, only_audio = type.value == Type.AUDIO.value).first().download(filename=type.value)

VideoFileClip(Type.VIDEO.value).set_audio(AudioFileClip(Type.AUDIO.value)).write_videofile(TEMP_TITLE)

os.rename(TEMP_TITLE, TITLE)
shutil.rmtree(TEMP_PATH)