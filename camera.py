from picamera import PiCamera
from time import sleep, time
import os
import glob

camera = PiCamera()

video_length = 30
max_videos = 100
video_path = "/home/lmaxwell/Desktop/videos"

while True:
	video_filename = os.path.join(video_path, f'video_{int(time())}.h264')
	print("Recording {video_filename}")

	camera.start_recording(video_filename)
	sleep(video_length)
	camera.stop_recording()

	all_videos = sorted(glob.glob(f"{video_path}/*.h264"))

	if (len(all_videos) > max_videos):
		oldest_video = all_videos[0]
		os.remove(oldest_video)
