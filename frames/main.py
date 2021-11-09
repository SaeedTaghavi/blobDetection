import cv2
frames = []
# vidcap = cv2.VideoCapture('2021-10-21_15-26-51.mp4')
filename ='test1_Y-Z.mp4'
vidcap = cv2.VideoCapture('test1_Y-Z.mp4')
success,image = vidcap.read()
frames.append(image)
count = 0
while success:
  # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: %d ' % count, success)
  frames.append(image)
  count += 1
print ("num frames: ", len(frames))