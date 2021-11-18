import os
import cv2
import  math
import numpy as np

# def MSD()
#     r = np.sqrt(xdata**2 + ydata**2)
#     diff = np.diff(r) #this calculates r(t + dt) - r(t)
#     diff_sq = diff**2
#     MSD = np.mean(diff_sq)

def findCM(frame, showImagesEnable=False):
    # read the image
    # fullPath='./frames/frame0.jpg'
    # image = cv2.imread(fullPath)
    image = frame
    # B, G, R channel splitting
    blue, green, red = cv2.split(image)
    ret, thresh = cv2.threshold(blue, 50, 255, cv2.THRESH_BINARY_INV)
    ret, threshr = cv2.threshold(red, 50, 255, cv2.THRESH_BINARY)
    threshm = thresh*threshr
    contours3, hierarchy3 = cv2.findContours(image=threshm, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    # print("num contours: ",len(contours3))
    c = max(contours3, key = cv2.contourArea)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    if (showImagesEnable):
        # print(contours3)
        # draw contours on the original image
        image_contour_red = image.copy()
        cv2.drawContours(image=image_contour_red, contours=c, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        # see the results
        cv2.circle(image_contour_red, (cX, cY), 5, (255, 255, 255), -1)   #center of mass contour
        # x,y,w,h = cv2.boundingRect(c)
        # cv2.rectangle(image_contour_red,(x,y),(x+w,y+h),(0,255,0),2)
        # rect = cv2.minAreaRect(c)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(image_contour_red,[box],0,(0,0,255),2)
        # ellipse = cv2.fitEllipse(c)
        # cv2.ellipse(image_contour_red,ellipse,(0,255,0),2)
        
        cv2.imshow("f", image_contour_red)
        cv2.waitKey(0)
        cv2.imwrite('red_channel.jpg', image_contour_red)
        cv2.destroyAllWindows()
    return cX, cY

def get_frame_from_video(filePath,framNum):
    video_capture = cv2.VideoCapture(filePath)
    video_length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    # print(video_length)
    if (framNum<video_length):
        video_capture.set(1,framNum) #set frame number 
        ret, frame = video_capture.read() 
    else:
        print("framNum is more than video length")
        return None
    return frame

def count_total_frames(filePath):
    video_capture = cv2.VideoCapture(filePath)
    video_length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    return video_length

def loop_over_all_frames(filePath):
    centerFile=filePath.split('.')[0]+".txt"
    if (os.path.exists(centerFile)):
        os.remove(centerFile)
    f = open(centerFile, "a")
    numFrames = count_total_frames(filePath)
    # print("numFrames: ",numFrames)
    for iFrame in range(numFrames):
    # for iFrame in range(100):
        frame = get_frame_from_video(filePath,iFrame)
        if (frame is not None ):
            x,y = findCM(frame)
            f.write(' %d , %d , %d \n' %(iFrame, x,y))
            print( iFrame, x , y )
    f.close()


# filePath ='test1_Y-Z.mp4'
# loop_over_all_frames(filePath)


    






