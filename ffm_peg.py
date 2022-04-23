import sys
sys.path.append(r'C:/Users/ffmpeg/bin')

import ffmpeg #cannot be used simply as this need to provide path to ffmpeg files




# print(a)
sys.path

# input video file

stream = ffmpeg.input('V.mp4')


stream = ffmpeg.filter(stream, 'fps', fps=10, round='up')
stream = ffmpeg.output(stream, 'dummy100.mp4')
ffmpeg.run(stream)

# stream = stream.trim(start = 10 ,duration = 15)
# print(stream)
# stream = stream.filter('fps',fps =5 , round = 'up').filter('scale', w = 128 , h = 128)
# print(stream)
# stream = ffmpeg.output(stream, 'output.mp4')
# print(stream)

# ffmpeg.run(stream)