

# from PIL import Image


# im = Image.open(r'W:\TEST\frames\999.jpg')


# xmin= 0
# ymax = 486
# xmax= 260
# ymin = 309

# im1 = im.crop((xmin, ymin, xmax,ymax ))
 
# # Shows the image in image viewer

# im1.show('W:\TEST/frames_cropped\999.jpg')

# import os

# import ffmpeg
# import subprocess
# # os.system('ffprobe -v 0 -of compact=p=0 -select_streams 0 \ -show_entries stream=r_frame_rate W:\TEST\concatenate.mp4')
# # print(r_frame_rate)
# a = os.system("ffmpeg  -i W:\TEST\concatenate.mp4")
# print("@@@@@@@@@@@@@@@@@@@@")
# print(a)
# (out, err) = a.communicate()
# (out, err) = a.communicate()
# print(out)
# p = subprocess.Popen(a, stdout=subprocess.PIPE)

# out, err = p.communicate()
# print(out)

# probe = ffmpeg.probe('concatenate.mp4')
# video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
# fps = int(video_info['r_frame_rate'].split('/')[0])

# print(fps)


# def get_length(filename):

def get_video_lenght(filename):
    import subprocess

    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return(float(result.stdout))


# a = get_length('W:\TEST\concatenate.mp4')
# print(a)