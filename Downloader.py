#This code is unoptimised unsorted garbage, but it works, I needed to download one specific video so I probably also won't be working on this anymore.
#Use the one on the main branch if your video has no such restrictions.

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

# Download video and audio
def download(options):
    with YoutubeDL(options) as ydl:
        ydl.download(URL)

download(video)
download(audio)

# Specify the codec for the output video
video_codec = 'libx264'  # You can change this codec if needed

# Create a video clip from the video file
video_clip = VideoFileClip(f'video{EXTENSION}')

# Create an audio clip from the audio file
audio_clip = AudioFileClip(f'audio{EXTENSION}')

# Set the audio of the video clip
video_clip = video_clip.set_audio(audio_clip)

# Write the video file with the specified codec
video_clip.write_videofile('agony.mp4', codec=video_codec)

# Close the clips
video_clip.close()
audio_clip.close()