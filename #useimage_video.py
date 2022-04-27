from moviepy.editor import *
import os
from moviepy.editor import *
import os



count = os.listdir(r'W:\TEST\frames_cropped')
print((count[-1]))
# clips = []

count_numbers = [i.replace('.jpg','') for i in count]
a = []
for  i in range(0, len(count_numbers)):
    a.append(count_numbers[i])
    
print(a) #the files are not sorted

a.sort(key = int)# this will sort the files inside the array
print(a) 


a = [i + '.jpg' for i in a] #giving back jpg to the files

print(a)
clips = []
for i in range(0,len(a)):
    clip = ImageClip(r'W:\TEST\\frames_cropped\\'  + a[i]).set_duration(0.017)
    clips.append(clip)
    print(i)


video_clip = concatenate_videoclips(clips,method ='compose')
video_clip.write_videofile('frameconcatenated.mp4', fps = 60)
# os.system('ffmpeg -r 1/5 -i W:/TEST/frames_cropped/%d.jpg -c:v libx264 -vf "fps=60,format=yuv420p" out.mp4')

# for i in range(0,len(count)):
#     print(count[i])
#     clip = ImageClip(r'W:\TEST\\frames_cropped' + '\\' + count[i]).set_duration(0.017)
#     clips.append(clip)
#     print(i)

# print(clips)

# video_clip = concatenate_videoclips(clips,method ='compose')
# video_clip.write_videofile('frameconcatenated.mp4', fps = 60, remove_temp = True, codec ="libx264")
