from moviepy.editor import *
import os


count = os.listdir(r'W:\TEST\frames_cropped')
print((count[0]))
clips = []
for i in range(0,len(count)):
    clip = ImageClip(r'W:\TEST\\frames_cropped' + '\\' + count[i]).set_duration(0.017)
    clips.append(clip)
    print(i)

video_clip = concatenate_videoclips(clips,method ='compose')
video_clip.write_videofile('frameconcatenated.mp4', fps = 60)