import pytube

VIDEO_URL = """
https://youtu.be/lz156C981fs
"""

yt = pytube.YouTube(VIDEO_URL)
stream = yt.streams.filter(only_audio=True).first()
stream = yt.streams.filter(only_video=True).first()
stream.download()