from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip, AudioFileClip

URL = ["https://youtu.be/nwPtcqcqz00"]
EXTENSION = '.webm'

video = {
    'format': 'bestvideo',  
    'outtmpl': 'video.%(ext)s', 
}

audio = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
}

#title = ''

def download(options):
    with YoutubeDL(options) as ydl:
        ydl.download(URL)
        #global title
        #title = ydl.extract_info(URL, download=False).get('title', 'Title not available')
download(video)
download(audio)


VideoFileClip(f'video{EXTENSION}').set_audio(AudioFileClip(f'audio{EXTENSION}')).write_videofile('pain')
    