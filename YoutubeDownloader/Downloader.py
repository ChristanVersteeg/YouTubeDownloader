import os
import re
from enum import Enum
import pytube
from moviepy.editor import VideoFileClip, AudioFileClip

VIDEO_URL = """
https://youtu.be/lz156C981fs
"""
YT = pytube.YouTube(VIDEO_URL)

EXTENSION = ".mp4"
TEMP_PATH = "./Temp/"

#If you want it clean you could use TITLE = fr"{re.sub(r'[^\w\s]', '', YT.title)}{EXTENSION}",
TITLE = re.sub(r'[^\w\s]', '', YT.title) + EXTENSION 
TEMP_TITLE = f"{TEMP_PATH}{TITLE}"
#but that only works in Python 3.12, which is in pre-release.

class Type(Enum):
    VIDEO = f"{TEMP_PATH}video{EXTENSION}"
    AUDIO = f"{TEMP_PATH}audio{EXTENSION}"
    
for type in Type: YT.streams.filter(only_video = type.value == Type.VIDEO.value, only_audio = type.value == Type.AUDIO.value).first().download(filename=type.value)

VideoFileClip(Type.VIDEO.value).set_audio(AudioFileClip(Type.AUDIO.value)).write_videofile(TEMP_TITLE)

for type in Type: os.remove(type.value)
os.rename(TEMP_TITLE, TITLE)