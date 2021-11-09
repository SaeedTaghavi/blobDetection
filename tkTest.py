import tkinter
import tkinter.messagebox
import tkinter.filedialog

win = tkinter.Tk()
filename=""
def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

def findRedBlob():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

def selectVideo():
   filename = tkinter.filedialog.askopenfilename(filetypes=[("video files", "*.mp4"),("video files", "*.MP4"),("All files", "*.*")])
   print(filename)

C = tkinter.Button(win, text ="select video", command = selectVideo)
B = tkinter.Button(win, text ="Hello", command = findRedBlob)

# C.pack()
# B.pack()

win.mainloop()