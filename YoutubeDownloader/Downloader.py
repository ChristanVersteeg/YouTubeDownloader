import os
import re
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
VIDEO = f"{TEMP_PATH}video{EXTENSION}"
AUDIO = f"{TEMP_PATH}audio{EXTENSION}"

def download(filename): YT.streams.filter(only_video = filename == VIDEO, only_audio = filename == AUDIO).first().download(filename=filename)
download(VIDEO)
download(AUDIO)

VideoFileClip(VIDEO).set_audio(AudioFileClip(AUDIO)).write_videofile(TEMP_TITLE)
os.remove(VIDEO)
os.remove(AUDIO)
os.rename(TEMP_TITLE, TITLE)