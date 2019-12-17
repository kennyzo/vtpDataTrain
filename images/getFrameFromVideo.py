import cv2
import time
import os
vidcap = cv2.VideoCapture('source_videos/M02-20191203-8h49.mp4')
success,image = vidcap.read()
count = 0
path = "source_images" + "/M02-20191203-8h49"
os.mkdir(path)
while success:
  if count < 10:
    cv2.imwrite(path + "/M02-20191203-8h49-000%d.jpg" % count, image)     # save frame as JPEG file      
  elif count < 100:  
    cv2.imwrite(path + "/M02-20191203-8h49-00%d.jpg" % count, image)     # save frame as JPEG file        
  elif count < 1000:
    cv2.imwrite(path + "/M02-20191203-8h49-0%d.jpg" % count, image)     # save frame as JPEG file        
  else:
        cv2.imwrite(path + "/M02-20191203-8h49-%d.jpg" % count, image)     # save frame as JPEG file        
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  #time.sleep()
  count += 1

