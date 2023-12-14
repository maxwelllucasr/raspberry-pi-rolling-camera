from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
from libcamera import Transform
import time
import os
import glob
import subprocess

video_length_seconds = 10 * 60  # 10 minutes
max_videos = 500
video_path = "/videos"  # Replace with your desired path

# Ensure video directory exists
if not os.path.exists(video_path):
    os.makedirs(video_path)

# Initialize camera
picam2 = Picamera2()
video_config = picam2.create_video_configuration(transform=Transform(rotation=0))
picam2.configure(video_config)

# Function to manage video files
def trim_videos():
    all_h264_videos = glob.glob(os.path.join(video_path, "*.h264"))
    for h264 in all_h264_videos:
        os.remove(h264)

    all_videos = sorted(glob.glob(os.path.join(video_path, "*.mp4")))
    while len(all_videos) > max_videos:
        os.remove(all_videos.pop(0))  # Remove the oldest video

trim_videos()

# Main loop
while True:
    timestamp = int(time.time())
    h264_filename = os.path.join(video_path, f'video_{timestamp}.h264')
    mp4_filename = os.path.join(video_path, f'video_{timestamp}.mp4')

    # Start recording
    encoder = H264Encoder(bitrate=100000)  # Adjust bitrate as needed
    picam2.start_recording(encoder, h264_filename)
    time.sleep(video_length_seconds)
    picam2.stop_recording()

    # Convert to MP4
    subprocess.run(["MP4Box", "-add", h264_filename, mp4_filename])
    os.remove(h264_filename)

    # Trim older videos
    trim_videos()
