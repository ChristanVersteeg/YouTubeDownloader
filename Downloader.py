#Made by Christan Versteeg; https://github.com/ChristanVersteeg/YouTubeDownloader

import os
from re import sub
from shutil import rmtree
from pytube import YouTube
from enum import Enum
from moviepy.editor import VideoFileClip, AudioFileClip
from ctypes import windll

YT = YouTube("""
https://youtu.be/dQw4w9WgXcQ
""")

EXTENSION = ".mp4"
TEMP_PATH = "Temp/"
EXPORTS_PATH = "Exports/"

def mkdir_not_exists(path): os.mkdir(path) if not os.path.exists(path) else None

mkdir_not_exists(TEMP_PATH)
windll.kernel32.SetFileAttributesW(TEMP_PATH, 0x2)
mkdir_not_exists(EXPORTS_PATH)

#If you want it clean you could use TITLE = fr"{sub(r'[^\w\s]', '', YT.title)}{EXTENSION}",
TITLE = sub(r'[^\w\s]', '', YT.title) + EXTENSION 
TEMP_TITLE = f"{TEMP_PATH}{TITLE}"
#but that only works in Python 3.12, which is in pre-release.

if os.path.exists(f"{EXPORTS_PATH}{TITLE}"): os.remove(f"{EXPORTS_PATH}{TITLE}")

class Type(Enum):
    VIDEO = f"{TEMP_PATH}video{EXTENSION}"
    AUDIO = f"{TEMP_PATH}audio{EXTENSION}"
    
for type in Type: YT.streams.filter(only_video = type.value == Type.VIDEO.value, only_audio = type.value == Type.AUDIO.value).first().download(filename=type.value)

VideoFileClip(Type.VIDEO.value).set_audio(AudioFileClip(Type.AUDIO.value)).write_videofile(f"{EXPORTS_PATH}{TITLE}", temp_audiofile=TEMP_TITLE)

rmtree(TEMP_PATH)