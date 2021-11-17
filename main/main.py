from lib import *
import tkinter
import tkinter.messagebox
import tkinter.filedialog



filename=""
win = tkinter.Tk()
win.geometry("800x600")
numCols = 4

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

def selectVideo():
   global filename
   filename = tkinter.filedialog.askopenfilename(filetypes=[("video files", "*.mp4"),("video files", "*.MP4"),("All files", "*.*")])
   tkinter.Label(win, text= "video file path: " + filename, font= ('Helvetica 10')).grid(row=2, column=0 , columnspan=numCols, padx= 20, pady= 10)   

def selectPhoto():
   global filename
   filename = tkinter.filedialog.askopenfilename(filetypes=[("image files", "*.jpg"),("All files", "*.*")])
   tkinter.Label(win, text= "file path : " + filename, font= ('Helvetica 10')).grid(row=2, column=0 , columnspan=numCols, padx= 20, pady= 10)   

def process():
   global filename
   loop_over_all_frames(filename)
#create an instance of tkinter frame
#Create some Button widgets
tkinter.Button(win, text= "select one photo", command=selectPhoto).grid(row=0, column=0, padx= 20, pady= 10)
tkinter.Button(win, text= "select video", command=selectVideo).grid(row=0, column=2, padx= 20, pady =10)
tkinter.Button(win, text= "process", command=process).grid(row=4, column=0, padx= 20, pady =10)


win.mainloop()