import cv2
filename ='test1_X-Z.mp4'
vidcap = cv2.VideoCapture(filename)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: %d ' % count, success)
  count += 1
print ("num frames: ", len(frames))