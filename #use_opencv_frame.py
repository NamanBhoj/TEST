import cv2
import os

vid = cv2.VideoCapture("W:\TEST\concatenate.mp4")




if not os.path.exists('frames'):
    os.mkdir('frames')

currentframe = 0 
while True:
    success, frame = vid.read()
    # cv2.imshow('output', frame)
    print(currentframe)
    cv2.imwrite(f'W:/TEST/frames/{currentframe}'+ '.jpg',frame)
    currentframe = currentframe +1
    print(currentframe)
# vid.release()
# cv2.destroyAllWindows()



