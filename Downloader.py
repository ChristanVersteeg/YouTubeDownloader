#Made by Christan Versteeg; https://github.com/ChristanVersteeg/python_projects/tree/main/YoutubeDownloader

import os
from re import sub
from shutil import rmtree
from pytube import YouTube
from enum import Enum
from moviepy.editor import VideoFileClip, AudioFileClip
from ctypes import windll

YT = YouTube("""
https://youtu.be/lz156C981fs
""")

EXTENSION = ".mp4"
TEMP_PATH = "Temp/"

if not os.path.exists(TEMP_PATH): os.mkdir(TEMP_PATH)
windll.kernel32.SetFileAttributesW(TEMP_PATH, 0x2)

#If you want it clean you could use TITLE = fr"{re.sub(r'[^\w\s]', '', YT.title)}{EXTENSION}",
TITLE = sub(r'[^\w\s]', '', YT.title) + EXTENSION 
TEMP_TITLE = f"{TEMP_PATH}{TITLE}"
#but that only works in Python 3.12, which is in pre-release.

if os.path.exists(TITLE): os.remove(TITLE)

class Type(Enum):
    VIDEO = f"{TEMP_PATH}video{EXTENSION}"
    AUDIO = f"{TEMP_PATH}audio{EXTENSION}"
    
for type in Type: YT.streams.filter(only_video = type.value == Type.VIDEO.value, only_audio = type.value == Type.AUDIO.value).first().download(filename=type.value)

VideoFileClip(Type.VIDEO.value).set_audio(AudioFileClip(Type.AUDIO.value)).write_videofile(TEMP_TITLE)

os.rename(TEMP_TITLE, TITLE)
rmtree(TEMP_PATH)