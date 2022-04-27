from cgitb import small
import logging
import os
import argparse
import pandas
import json
from pprint import pprint
from moviepy.editor import concatenate_videoclips, VideoFileClip
from PIL import Image
from moviepy.editor import *
import os

"""cut out face and center videos """

"""merge both the vids with the face vid being at the top right"""

""" align for tiktok video 1080 * 1920"""

"""
CROP
OVERLAY
THEN APPLY 1080*1920
DYNAMIC FACE CAM COORDINATE FUNCTIONALITY --> FIGURE OUT, ADD START AND END FOR THE COORDINATE CHANGES

SEGMENT1+ SEGMENT2 ... SEGN = VIDEO
"""






def readjson_coordinates_face(data):
    x_min_ar = []
    x_max_ar = []
    y_min_ar = []
    y_max_ar = []
    all = []
    """reads the json file and extracts minimum and maximum values,
     finally returns them  as a tuple (xmin, xmax, ymin, ymax)"""

    """The x coordinate and y coordinate are zero at the left top"""

    #open json file
    f = open (data, "r")
    #read and save data in datas
    datas = json.loads(f.read())

    #check frame by frame i.e index by index
    try:
        for i in range(0,len(datas['x1'])) :
        # Coordinates
            x_min = datas['x1'][str(i)]
            x_min_ar.append(x_min)
            x_max = datas['x2'][str(i)]
            x_max_ar.append(x_max)
            y_min = datas['y1'][(str(i))]
            y_min_ar.append(y_min)
            y_max = datas['y2'][str(i)]
            y_max_ar.append(y_max)
        
        all.append(x_min_ar)
        all.append(y_min_ar)
        all.append(x_max_ar)
        all.append(y_max_ar)
    except KeyError:
        print("You got a key wrong, check the json file for key structure")

    #close file
    finally:
        f.close()

    #storing values in a tuple
    # values = (int(x_min_ar)  , int(y_min_ar),int(x_max_ar), int(y_max_ar))
   
    return all



def readjson_coordinates_center(data):
    """The x coordinate and y coordinate are zero at the left top"""
    x_min_ar = []
    x_max_ar = []
    y_min_ar = []
    y_max_ar = []
    all = []

    #open json file
    f = open (data, "r")
    #read and save data in datas
    datas = json.loads(f.read())

    
    try:
        for  i in range(0, len(datas['rect_x1'])):
        # Coordinates
            x_min = datas['rect_x1']['0']
            x_min_ar.append(x_min)
            x_max = datas['tect_x2']['0']#TODO CORRECT IT AS rect_x2 for o/p in webcam_center_detection
            x_max_ar.append(x_max)
            y_min = datas['rect_y1']['0']
            y_min_ar.append(y_min)
            y_max = datas['rect_y2']['0'] 
            y_max_ar.append(y_max)

        all.append(x_min_ar)
        all.append(y_min_ar)
        all.append(x_max_ar)
        all.append(y_max_ar)
        
    except KeyError:
        print("You got a key wrong, check the json file for key structure")

    #close file
    finally:
        f.close()

    # storing values in a tuple
   
    return all





def crop_face(video,coordinate_data):
    
    import os
    values = readjson_coordinates_face(coordinate_data)
    # length = readjson_coordinates_center(length_json)
    # the first two arguments in crop are the width and height of the o/p video the other two are position to start
    #we define the o/p based on xmax-xmin whereas starting point is defined by xmin and ymin
    #TODO Read documentation here : https://ffmpeg.org/ffmpeg-filters.html#crop
    
    #TODO: EXTRACTING  FRAME CODE
    # os.system(' mkdir frames')
    # os.system(f'ffmpeg -i {video} frames/%d.jpg')
    # # print((len(values[0]))) #array with 4 list element x1,y1,x2,y2 values

    # # TODO: Code for cropping of frame images in frames folder images framewise
    # print(values[0])
    # os.system(' mkdir frames_cropped')
    
    # # print(image_path_save)
    # for i in range(1,len(values[0])):
    #     print("running")
    
       
    #     im = Image.open(f'W:\TEST\\frames\{i}.jpg')

    #     # im1 = im.crop((xmin, ymin, xmax, ymax))
    #     im1 = im.crop((values[0][i], values[1][i], values[2][i], values[3][i]))
    #     im1.save(f'frames_cropped\\{i}.jpg')

    # os.system(" rm -rf frames")
    count = os.listdir(r'W:\TEST\frames_cropped_concatenate')
    print((count[-1]))
    count_numbers = [i.replace('.jpg','') for i in count]
    a = []
    for  i in range(0, len(count_numbers)):
        a.append(count_numbers[i])
    
    print(a) #the files are not sorted

    a.sort(key = int)# this will sort the files inside the array
    print(a) 


    a = [i + '.jpg' for i in a]
    print(a)
    clips = []
    for i in range(0,len(a)):
        clip = ImageClip(r'W:\TEST\\frames_cropped_concatenate\\'  + a[i]).set_duration(0.017)
        clips.append(clip)
        print(i)


    video_clip = concatenate_videoclips(clips,method ='compose')
    video_clip.write_videofile('27-04-2022.mp4', fps = 60)


    #TODO: Create video from cropped frames and after that delete both frames and frames_cropped
    
  



    # TODO: OLDSOLUTION
    # for i in range(0, len(length[0]),600):

    #     output_x = values[2][i]- values[0][i]
    #     output_y = values[3][i] - values[1][i]
    #     output_x = values[2][i]- values[0][i] 
    #     pprint(output_x)
    #     output_y = values[3][i] - values[1][i]
    #     pprint(output_y)
    #     filenames.append(f"concatenatecropped{i}.mp4")
    #     os.system(f'ffmpeg -i {video} -vf crop={output_x}:{output_y}:{values[0][i]}:{values[1][i]} concatenatecropped{i}.mp4')

    #     print(filenames)
    # result_clip = concatenate_videoclips([VideoFileClip('concatenatecropped0.mp4'), VideoFileClip('concatenatecropped600.mp4')])
    # result_clip.write_videofile('merged.mp4')

   

def crop_centre(video,video_opname,coordinate_data):
    # op_name = 'cropped+center' + video[:-4]

    
    import os
    values = readjson_coordinates_center(coordinate_data)
    # print(values[0])
    tiktok_x = 9
    tiktok_y = 16
        # width_crop = values[2][0]-values[0][0]
    # height_crop = values[3][0]-values[1][0]
    #TODO: read reference https://www.linuxuprising.com/2020/01/ffmpeg-how-to-crop-videos-with-examples.html
    #https://video.stackexchange.com/questions/4563/how-can-i-crop-a-video-with-ffmpeg
    # os.system(f"ffmpeg -i {video} -vf crop=iw/2 {video_opname}")
    os.system(f"ffmpeg -i {video} -vf crop={values[0][0]}:{values[1][0]} -aspect 9:16 centercroppedvideo.mp4")
    # #TODO SCALE TO 1080 * 1920

def video_overlay(bigvid,smallvid):
    import os
    print(smallvid)
    #TODO: KEEP THE SMALL VID AS SAME DIRECTORY AS THIS FILE
    os.system(f'ffmpeg -i {bigvid} -vf "movie={smallvid},scale=150:-1[inner];[in][inner] overlay=main_w-(overlay_w+10):10"  overlay.mp4')


def video_9_16(videopath):
#https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
    os.system(f"ffmpeg -i {videopath} -vf scale=1080:1920  overlay1.mp4")



# crop_face(r'W:\TEST\clip5.mp4',r'W:\TEST\fileface.json')
# crop_centre(r'W:\TEST\concatenate.mp4',"testingvideo.mp4",r'W:\TEST\filecenter_concatenate.json')

# video_overlay(r'W:\TEST\centercroppedvideo.mp4',r'27-04-2022.mp4')

video_9_16(r"W:\TEST\overlay.mp4")





    
