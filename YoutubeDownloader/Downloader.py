import pytube
import moviepy.editor as mp
import os

VIDEO_URL = "https://youtu.be/g5DGJINVYxc?list=PLBAb9rF2kkJTppxPwzSeogOXcfHceSJC3"

output_file = "disc.ogg"

yt = pytube.YouTube(VIDEO_URL)
stream = yt.streams.filter(only_audio=True).first()
stream.download()

clip = mp.AudioFileClip(stream.default_filename)
clip.write_audiofile(output_file)
clip.close()

os.remove(stream.default_filename)