import os
import ffmpeg
os.system(f"ffmpeg -r 1 -i frames_cropped/frames_cropped1.jpg -vcodec mpeg4 -y croppedframes.mp4")