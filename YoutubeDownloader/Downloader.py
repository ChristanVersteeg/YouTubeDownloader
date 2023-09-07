import pytube

VIDEO_URL = """
https://youtu.be/lz156C981fs
"""

yt = pytube.YouTube(VIDEO_URL)
stream = yt.streams.get_highest_resolution()
stream.download()