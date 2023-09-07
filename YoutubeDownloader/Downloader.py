import os
import re
import pytube
from moviepy.editor import VideoFileClip, AudioFileClip

VIDEO_URL = """
https://youtu.be/lz156C981fs
"""
YT = pytube.YouTube(VIDEO_URL)
EXTENSION = ".mp4"
VIDEO = f"video{EXTENSION}"
AUDIO = f"audio{EXTENSION}"
TITLE = re.sub(r'[^\w\s]', '', YT.title) + EXTENSION

def download(filename): YT.streams.filter(only_video = filename == VIDEO, only_audio = filename == AUDIO).first().download(filename=filename)
download(VIDEO)
download(AUDIO)

VideoFileClip(VIDEO).set_audio(AudioFileClip(AUDIO)).write_videofile(TITLE)
os.remove(VIDEO)
os.remove(AUDIO)