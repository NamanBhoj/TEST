from cgitb import small
import logging
import pandas
import json
from pprint import pprint
from moviepy.editor import concatenate_videoclips, VideoFileClip
from PIL import Image
from moviepy.editor import *
import os
import argparse
import cv2

#TODO: Remove file with existing name if use provided that name already
"""cut out face and center videos using frame based approach """

"""merge both the vids with the face vid being at the top right"""

""" align for tiktok video 1080 * 1920"""

"""delete all exisiting files made in the process[not necessary]"""

PATH = os.getcwd()
print(PATH)

print(os.path.isdir('frames_cropped'))

def get_video_length(filename):
    import subprocess

    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return (float(result.stdout))

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





def crop_face(video,webcam_coordinate_data,smallvidname):
    
    import os
    values = readjson_coordinates_face(webcam_coordinate_data)
  
    #ERROR RESOLVED BY BELOW LINE, ERROR OF NOT DIVISIBLE BY 2 
    
    #TODO Read documentation here : https://ffmpeg.org/ffmpeg-filters.html#crop
    
    #TODO: EXTRACTING  FRAME CODE
    print("FRAME CREATING STARTED")
    os.system(f' mkdir {smallvidname}frames')

    #TODO:use open cv to create frames instead of ffmpeg
    #-vsync 2 is added for removing fmore than 1000 frames duplicated warninqg/erro
    print("EXTRACTION OF FRAMES STARTED")
    cap = cv2.VideoCapture(video)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        print(f'FRAME {count} created')
        if not ret:
            continue
        # Write the results back to output location.
        cv2.imwrite(f"{smallvidname}frames/%d.jpg" % (count+1), frame)
        count = count + 1
        if (count > (video_length-1)):
            # Log the time again
          
            # Release the feed
            cap.release()
            print(f" FRAME CREATION ENDED, CREATED FRAMES ARE AT {smallvidname}frames")

    # os.system(f'ffmpeg -i {video} -vsync 2 {smallvidname}frames/%d.jpg') #creates frames for video inside folder {smallvidname}frames
    
    # import time
    # time.sleep(1)
    # # # TODO: Code for cropping of frame images in frames folder images framewise
    # print(values[0])
    os.system(f' mkdir {smallvidname}frames_cropped')

    if os.path.isdir('Bigvid') == False:
        os.system(f'mkdir Bigvid')
        print("created Bigvid")

    if os.path.isdir('Smallvid') == False:
        os.system(f'mkdir Smallvid')
        print("created Bigvid")

    if os.path.isdir('Overlay') == False:
        os.system(f'mkdir Overlay')
        print("created Overlay")

    if os.path.isdir('Finalvid') == False:
        os.system(f'mkdir Finalvid')  
        print("created Finalvid")  


    
    #TODO: INSTEAD OF ITERATING ON VALUE ITERATE ON FRAME VALUE
    # print((values[0]))
    count1 = os.listdir(f'W:\TEST\{smallvidname}frames')
    print(len(count1))
    if len(count1) < len(values[0]):
        iterate_times = len(count1)
    else:
        iterate_times = len(values[0])

    #TODO: IF REMOVE THE -10 IN RANGE GET ERROR
    for i in range(1,iterate_times):
        print(f"CROPPING WEBCAM PART OF FRAME {i} AND SAVING IT TO {smallvidname}frames_cropped")
    
       
        im = Image.open(f'W:\TEST\\{smallvidname}frames\{i}.jpg')

        # im1 = im.crop((xmin, ymin, xmax, ymax))
        im1 = im.crop((values[0][i], values[1][i], values[2][i], values[3][i]))
        im1.save(f'{smallvidname}frames_cropped\\{i}.jpg')
    print(f"ALL THE FRAMES HAVE BEEN CROPPED AND SAVED TO {smallvidname}frames_cropped")


    #TODO: TO SORT THE CLIPS OTHERWISE WHEN RETRIEVED ARE UNSORTED, TO UNDERSTAND RUN LINE 148 AND 149 ONLY
    count = os.listdir(f'W:\TEST\{smallvidname}frames_cropped')
    print((count[-1]))
    count_numbers = [i.replace('.jpg','') for i in count]
    a = []
    for  i in range(0, len(count_numbers)):
        a.append(count_numbers[i])
    
    print(a) #the files are not sorted
    # # TODO:SORTS INTEGER STRING AND THEN WE WILL ADD .JPG AGAIN LATER
    a.sort(key = int)# this will sort the files inside the array
    print(a) 


    a = [i + '.jpg' for i in a]
    print(a)

    #TODO: MAKE VIDEO OUT OF FRAMES
    clips = []
    #USING THE FUNCTION get_video_length
    length = get_video_length(video)
    fps_val = len(a)/ length
    print(f"THIS IS A {fps_val} FPS VIDEO WITH TOTAL WATCHTIME OF {length} and has about {len(a)} FRAMES")
    print(1/fps_val)
    for i in range(0,len(a)):
        #FORMULA FOR SET DURATION OF EACH FRAME IS 1/FPS VALUE OF THE INPUT VIDEO
   
        clip = ImageClip(f'W:\TEST\\{smallvidname}frames_cropped\\'  + a[i]).set_duration(1/fps_val)
        clips.append(clip)
        # print(i)


    video_clip = concatenate_videoclips(clips,method ='compose')
    video_clip.write_videofile(f'Smallvid/{smallvidname}', fps = fps_val)
    # os.system(f"ffmpeg -i Smallvid/{smallvidname} -vf scale=400:400  Smallvid/{smallvidname[:-4]}.mp4")

    print(f"THE PROCESS TO CREATE WEBCAM VIDEO {smallvidname} HAS ENDED")
    print("BEGINNING CREATION OF CENTER CLIPS")
  


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

   

def crop_centre(video,center_coordinate_data,bigvidname):
    # op_name = 'cropped+center' + video[:-4]
    print(f"CENTER CLIP CREATION {bigvidname} HAS STARTED")

    
    import os
    values = readjson_coordinates_center(center_coordinate_data)
    # print(values[0])
    tiktok_x = 9
    tiktok_y = 16
    width_crop = values[2][0]-values[0][0]
    height_crop = values[3][0]-values[1][0]
    #TODO: read reference https://www.linuxuprising.com/2020/01/ffmpeg-how-to-crop-videos-with-examples.html
    #https://video.stackexchange.com/questions/4563/how-can-i-crop-a-video-with-ffmpeg
    # os.system(f"ffmpeg -i {video} -vf crop=iw/2 {video_opname}")
    os.system(f"ffmpeg -i {video} -vf crop={values[0][0]}:{values[1][0]} -aspect 9:16 Bigvid/{bigvidname}")
    # os.system(f"ffmpeg -i Bigvid/{bigvidname} -vf scale=1080:1920  Bigvid/{bigvidname[:-4]}.mp4")
    print(f"CENTER CLIP CREATION HAS ENDED. CREATED A VIDEO NAMED {bigvidname}")

    #see first example here https://ffmpeg.org/ffmpeg-filters.html#cropdetect
    # os.system(f"ffmpeg -i {video} -vf crop={width_crop}+500:{height_crop}+500:{values[0][0]}:{values[1][0]} -aspect 9:16 centercroppedvideo1.mp4")
    # #TODO SCALE TO 1080 * 1920



def video_overlay_and_9_16(bigvidname,smallvidname,finalvidname):
    print(f"PROCESS TO OVERLAY {smallvidname} OVER {bigvidname} STARTED ")
    import os
    print(smallvidname)
    overlayed_name = f"OVERLAY{bigvidname[:-4]}_{smallvidname[:-4]}.mp4"
    #TODO: KEEP THE SMALL VID AS SAME DIRECTORY AS THIS FILE
    #scale=150:-1 ,,, main_w-(overlay_w+10):10
    os.system(f'ffmpeg -i Bigvid/{bigvidname} -vf  "movie=Smallvid/{smallvidname}, scale =100:-2[inner];[in][inner]  overlay=10:10"  Overlay/{overlayed_name}')
    # os.system(f'ffmpeg -i Bigvid/{bigvidname} -i Smallvid/{smallvidname} scale=2*iw:2*ih  , overlay=main_w-(overlay_w+10):10 [out]   Overlay/{overlayed_name}')
    print(f"OVERLAYED VIDEO {overlayed_name}")

    print(f"PROCESS TO SCALE VIDEO {overlayed_name} TO TIKTOK FORMAT STARTED")

    print(f"WILL CREATE VIDEO NAMED {finalvidname} ONCE THE PROCESS IS DONE")
    #https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
    os.system(f"ffmpeg -i Overlay/{overlayed_name} -vf scale=1080:1920  Finalvid/FINAL{finalvidname}.mp4")
    print(f"PROCESS ENDED FINAL VIDEO NAMED FINAL{finalvidname}.mp4 CREATED")
    



    
    
    


#master function to run everything
def master(video,webcam_coordinate_data,smallvidname,center_coordinate_data,bigvidname,finalvidname):
    # STEP1: has 3 different mini steps
    crop_face(video,webcam_coordinate_data,smallvidname)
    # STEP2:
    crop_centre(video,center_coordinate_data,bigvidname)
    # STEP3 and 4 included:
    video_overlay_and_9_16(bigvidname,smallvidname,finalvidname)

    print("THE WHOLE PIPELINE RAN SUCCESSFULLY")

# master('W:/TEST/concatenate.mp4','W:/TEST/fileface_concatenate.json',"smallvid.mp4",'W:/TEST/filecenter_concatenate.json',"bigvid.mp4","pipeline")
# crop_face(r'W:\TEST\recorded.mp4',r'W:\TEST\fileface_151.json',"recordedsmall.mp4")
# crop_centre(r'W:\TEST\concatenate.mp4',r'W:\TEST\filecenter_concatenate.json',"bigvid.mp4")
# video_overlay(r'bigvid.mp4',r'smallvid.mp4')
# video_9_16(r"W:\\TEST\\OVERLAYbigvi_smallvi.mp4", "FIFA")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Runs the Tiktok Video Creationg Pipeline")
    # parser.add_argument('--video',required= True)
    # parser.add_argument('--webcam_coordinate_data',required= True)
    # parser.add_argument('--smallvidname',required= True)
    # parser.add_argument('--center_coordinate_data',required= True)
    # parser.add_argument('--bigvidname',required= True)
    # parser.add_argument('--finalvidname',required= True)
    parser.add_argument('--v',required= True)
    parser.add_argument('--wcd',required= True)
    parser.add_argument('--svn',required= True)
    parser.add_argument('--ccd',required= True)
    parser.add_argument('--bvn',required= True)
    parser.add_argument('--fvn',required= True)
    args = parser.parse_args()


    # master(args.video,args.webcam_coordinate_data,args.smallvidname,args.center_coordinate_data,args.bigvidname,args.finalvidname)
    master(args.v,args.wcd,args.svn,args.ccd,args.bvn,args.fvn)

# master('W:/TEST/concatenate.mp4','W:/TEST/fileface_concatenate.json',"smallvid.mp4",'W:/TEST/filecenter_concatenate.json',"bigvid.mp4","pipeline")
    
