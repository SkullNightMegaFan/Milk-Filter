import cv2
import numpy as np
import os
import rawpy
from PIL import Image
from tkinter import *
from tkinter import ttk

#The user types out the name of the video they want to have put through the filter
#In future versions, I would work with the GUI so a person can just drag and drop their video file.

videoProcessor:  None
def select_videofile():
    set types = (
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.mp4'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.mov'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.mp4'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.wmv'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.mkv'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.avi'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.hevc'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.av1'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.avchd'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.mts'),
                        ('Video files (.mp4,.mov,.wmv,.mkv, .avi, .hevc, .av1, .avchd, .mts, .m2ts)', '*.m2ts'),
                    
                )
    set filename [tk_getOpenFile -filetypes $types]
    filename = fd.askopenfilename(title='Open a file',initialdir='.',filetypes=filetypes)
        if filename has video suffix:  
            videoProcessor = True;
    
        else:
            videoProcessor = False;

     
    img = Image.open(filename)
    resized_img = img.resize((int(widthWindow/2.2), int(heightWindow/2.2)), Image.Resampling.LANCZOS)
    imgTk = ImageTk.PhotoImage(resized_img)
    display.config(image=imgTk)
    display.image = imgTk
    window.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    
if 
selectedVideo = input('What is the name of the video file?\n');
print(selectedVideo);       
#Then the filter creates a directory where to put all the frames of video.
#I need to make it so that there's a mini preview of the entire video so people don't have to consume their entire video first.
os.mkdir(selectedVideo)
'''selectedVideo

#This definition cuts the video into individual frames and places those frames into it's own directory for easy navigation
def getFrames(string selectedVideo):
    video = cv2.VideoCapture(selectedVideo)
    #create readme file that has information about the video
    #such as avg frame rate, how many frames, length of video, resolution, etc.
    ok, frame = video.read()
    count = 0
    while ok:
        cv2.imwrite("frame%04d.jpg".format(count), frame)
        print('WRITTEN FRAME:', count)
        count+=1
        ok, frame = video.read()
    video.release()

#This definiton applies the filter to each frame in the video.
#Depending on the type of file format the filter will have variations in how it applies the filter.
def paintFrames():
    go into the selectedVideo directory
    os.mkdir(selectedVideo_FilterApplied)
    loop through the directory using a while loop to read each image
    apply filter to currently read frame.
    save frame in selectedVideo_FilterApplied
    Continuing looping until all images have been filtered.

#This definition places the painted frames back together, using the information from the readme file provided by the getFrames. People will also be allowed to insert custom settings so they can change the frame rate and experiment. 
def stichFrames():
    enter selectedVideo_FilterApplied directory
    read info from readme file or from player provided input.
    loop through directory,
    read each frame and add that to a new video file. 
    output the video file.

getFrames()        
    
    '''