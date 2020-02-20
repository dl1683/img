import cv2
import glob
import numpy as np
from tkinter import filedialog
from tkinter import *

import Imgs as iv
import Vids as vi

#pick Video file
#Vid-->imgs
#imgs-->texts
#texts-->imgs
#comparison functions
#new imgs-->vid
    
def main():
    """root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Img files","*.mp4 .mkv .avi"),("all files","*.*")))
    #print (root.filename)
    vi.convertVidToImg(root.filename)
    iv.convertImgToVid()
    """
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Img files","*.png .jpg .jpeg .jfif"),("all files","*.*")))
    height,width=iv.convertToText(root.filename)
    index=str(root.filename).index('.')
    ext=str(root.filename)[index:]
    
    #build both to compare
    iv.blackAndWhite(height,width,ext)
    iv.convertToImg(height,width,ext)
    r=r"C:\Users\Devansh\Desktop\Projects\img\tested.jpg" 
    
    #iv.processImg(r,'jpg')

main()