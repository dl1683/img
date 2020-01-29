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
    filename=r"C:\Users\Devansh\Desktop\Projects\img\test2.jpeg"
    height,width=iv.convertToText(filename)
    iv.convertToImg(height,width) 

main()