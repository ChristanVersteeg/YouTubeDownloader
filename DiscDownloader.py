from os import remove
from pytube import YouTube
from moviepy.editor import AudioFileClip

VIDEO_URL = """
https://youtu.be/qIzerUh9F-8
"""

stream = YouTube(VIDEO_URL).streams.filter(only_audio=True).first()
stream.download()

AudioFileClip(stream.default_filename).write_audiofile("disc.ogg")
remove(stream.default_filename)