from picamera import PiCamera, Color
from time import sleep, time
from datetime import datetime
import os
import glob
import subprocess

print("Starting camera")

camera = PiCamera()
camera.rotation = 180
camera.resolution = (640,480)
camera.annotate_background = Color("black")

video_length = 600
max_videos = 1000
video_path = "/videos"

while True:
	h264_filename = os.path.join(video_path, f'video_{int(time())}.h264')
	mp4_filename = os.path.join(video_path, f'video_{int(time())}.mp4')
	print(f'Recording {mp4_filename}')

	start_time = datetime.now()
	camera.start_recording(h264_filename, bitrate=250000)
	while (datetime.now() - start_time).seconds < video_length:
		camera.annotate_text = datetime.now().strftime("%H:%M:%S %D")
		sleep(.01)
	camera.stop_recording()

	#apt install gpac
	subprocess.run(["MP4Box", "-add", h264_filename, mp4_filename])

	os.remove(h264_filename)

	all_videos = sorted(glob.glob(f"{video_path}/*.mp4"))

	if (len(all_videos) >= max_videos):
		oldest_video = all_videos[0]
		os.remove(oldest_video)
