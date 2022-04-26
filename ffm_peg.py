import sys
sys.path.append(r'C:/Users/ffmpeg/bin')
import os
# os.system('ffmpeg -i V.mp4 -ss 00:00:10 -to 00:02:20 -c:v copy -c:a copy newfile.mp4')
os.system('ffmpeg -i clip3.mp4 -vf crop=1344:741:1890:1048 cropped.mp4')
# import ffmpeg #cannot be used simply as this need to provide path to ffmpeg files
# # stream = ffmpeg.filter(stream, 'fps', fps=10, round='up')
# audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
# video = input.video.hflip()
# stream = ffmpeg.output(audio, video, 'dummy100.mp4')
# ffmpeg.run(stream)


