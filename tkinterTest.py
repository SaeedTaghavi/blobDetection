import cv2
import  math
import numpy as np
#Import the required library
import tkinter
import tkinter.messagebox
import tkinter.filedialog


filenameXZ=""
filenameYZ=""
filename=""
win = tkinter.Tk()
win.geometry("800x600")
numCols = 4

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

def findContours():
   # fullPath='./frames/frame0.jpg'
   global filename
   fullPath=filename
   image = cv2.imread(fullPath)

   # B, G, R channel splitting
   blue, green, red = cv2.split(image)
   # print(np.shape(red))
   # cv2.imshow("red",red)
   # cv2.imshow("blue",blue)
   # cv2.imshow("green",green)
   # cv2.waitKey(0)

   # detect contours using blue channel and without thresholding
   contours1, hierarchy1 = cv2.findContours(image=blue, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
   # draw contours on the original image
   image_contour_blue = image.copy()
   cv2.drawContours(image=image_contour_blue, contours=contours1, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
   # see the results
   # cv2.imshow('Contour detection using blue channels only', image_contour_blue)
   # cv2.waitKey(0)
   # cv2.imwrite('blue_channel.jpg', image_contour_blue)
   # cv2.destroyAllWindows()

   # detect contours using green channel and without thresholding
   contours2, hierarchy2 = cv2.findContours(image=green, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
   # draw contours on the original image
   image_contour_green = image.copy()
   cv2.drawContours(image=image_contour_green, contours=contours2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
   # see the results
   # cv2.imshow('Contour detection using green channels only', image_contour_green)
   # cv2.waitKey(0)
   # cv2.imwrite('green_channel.jpg', image_contour_green)
   # cv2.destroyAllWindows()

   # detect contours using red channel and without thresholding
   # ret, thresh1 = cv2.threshold(blue, 50, 255, cv2.THRESH_BINARY_INV)
   ret, thresh = cv2.threshold(blue, 45, 255, cv2.THRESH_BINARY_INV)
   ret, threshr = cv2.threshold(red, 50, 255, cv2.THRESH_BINARY)
   threshm = thresh*threshr
   # cv2.imshow("r",threshr)
   # cv2.imshow("b",thresh)
   # cv2.imshow("r*b",threshm)
   # cv2.waitKey(0)
   # ret, thresh = cv2.threshold(red, 110, 120, cv2.THRESH_BINARY)
   contours3, hierarchy3 = cv2.findContours(image=threshm, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
   print("num contours: ",len(contours3))
   # draw contours on the original image
   image_contour_red = image.copy()
   cv2.drawContours(image=image_contour_red, contours=contours3, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
   # see the results
   cv2.imshow(fullPath, image_contour_red)
   cv2.waitKey(0)
   cv2.imwrite('red_channel.jpg', image_contour_red)
   cv2.destroyAllWindows()


def extractFramesFromVideo(filepath):
   frames=[]
   vidcap = cv2.VideoCapture(filepath)
   success,image = vidcap.read()
   frames.append(image)
   count=0
   while success:
      cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print("hi")
      print('Read a new frame: ', success)
      count += 1
      frames.append(image)
      return(frames)
def process():
   xz_frames = extractFramesFromVideo(filenameXZ)
   print(len(xz_frames))
   yz_frames = extractFramesFromVideo(filenameYZ)
   print(len(yz_frames))
def selectVideoXZ():
   global filenameXZ
   filenameXZ = tkinter.filedialog.askopenfilename(filetypes=[("video files", "*.mp4"),("video files", "*.MP4"),("All files", "*.*")])
   tkinter.Label(win, text= "file path xz: " + filenameXZ, font= ('Helvetica 10')).grid(row=1, column=0 , columnspan=numCols,padx= 20, pady= 10)   

def selectVideoYZ():
   global filenameYZ
   filenameYZ = tkinter.filedialog.askopenfilename(filetypes=[("video files", "*.mp4"),("video files", "*.MP4"),("All files", "*.*")])
   tkinter.Label(win, text= "file path yz: " + filenameYZ, font= ('Helvetica 10')).grid(row=2, column=0 , columnspan=numCols, padx= 20, pady= 10)   
def selectPhoto():
   global filename
   filename = tkinter.filedialog.askopenfilename(filetypes=[("image files", "*.jpg"),("All files", "*.*")])
   tkinter.Label(win, text= "file path : " + filename, font= ('Helvetica 10')).grid(row=2, column=0 , columnspan=numCols, padx= 20, pady= 10)   
#create an instance of tkinter frame
#Create some Button widgets
tkinter.Button(win, text= "select one photo", command=selectPhoto).grid(row=0, column=0, padx= 20, pady= 10)
tkinter.Button(win, text= "select video X-Z", command=selectVideoXZ).grid(row=0, column=2, padx= 20, pady =10)
tkinter.Button(win, text= "select video Y-Z", command=selectVideoYZ).grid(row=0, column=3, padx= 20, pady =10)
tkinter.Button(win, text= "find contours", command=findContours).grid(row=4, column=0, padx= 20, pady =10)
tkinter.Button(win, text= "process on videos", command=process).grid(row=4, column=1, padx= 20, pady =10)

win.mainloop()