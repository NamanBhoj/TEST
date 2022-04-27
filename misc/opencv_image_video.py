import cv2
import os
from PIL import Image
from numpy import full, number

path = 'W:/TEST/frames'

outpath = 'W:/TEST/'

vid_name = "opencv_image_video.mp4"

full_vid_path = outpath + vid_name

number_images = os.listdir(path)

#TODO: have to do this otherwise we were getting a problems like frame 5000.jpg before frame 99.jpg
number_images_number = [i.replace('.jpg','') for i in number_images]


# print('2.jpg' in number_images)
a = []
for  i in range(0, len(number_images_number)):

    a.append(number_images_number[i])

# print(a)

#TODO: have to do this otherwise we were getting a problems like frame 5000.jpg before frame 99.jpg
a.sort(key = int)
print(a)

a = [i + '.jpg' for i in a]

print(a[0])

# frame = cv2.imread(a[0])
# size = frame.shape
# print(size)
cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 60
video = cv2.VideoWriter(full_vid_path, cv2_fourcc, fps)

for  i in range(len(a)):
    video.write(cv2.imread(path + a[0]))

video.release()

# im = Image.open( path +'0.jpg')

# im.show(a[0])
     

    
   
#     a.append(number_images[i])

# print(a[4700:])