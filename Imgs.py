import glob
import cv2
import numpy as np
from txt import * 

def convertImgToVid():
    img_array = []
    for filename in glob.glob(r"C:\Users\Devansh\Desktop\Projects\img\data\*.jpg"):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    
    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def convertToText(img):
    """
    Send the img information into a text file. 
    @return:(row,col) of image
    """
    load=cv2.imread(img)
    height, width, layers = load.shape
    text=""
    #print(height,width, layers)
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt","w+")
    for i in range(height):
        for j in range(width):
            pixel=load[i,j]
            #text=text+(encode(str(pixel[0]))+encode(str(pixel[1]))+encode(str(pixel[2]))) #text
            #file1.write('\n')
    file1.write(text)

    return (height,width)

def convertToImg(height,width):
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt")
    blank_image = np.zeros((height,width,3), np.uint8)
    i=0 #height index
    j=0 #width index
    colors=list(file1.read())
    for index in range(0,len(colors),3):
            #TODO: Implement change to this to accomodate the lack of i,jif j<width,j++ else j=0,i++
        """info=line.split(",")   
        i,j=int(info[0]), int(info[1])
        colors=info[2]
        colors=colors.replace("[","").replace("]","").strip()
        colors=colors.split(" ")
        print("R: ",colors,info[2])
        if (str(colors[2])!=""):
            blank_image[i][j]=[int(colors[0]),int(colors[1]),int(colors[2])]
        else:
            blank_image[i][j]=[int(colors[0]),int(colors[1]),int(colors[3])]"""
        
        blank_image[i][j]=[int(decode(colors[index])),int(decode(colors[index+1])),int(decode(colors[index+2]))]
        if ( j<width-1 ):
            j+=1
        else:
            j=0
            i+=1
    cv2.imshow("Get Wrecked Shree", blank_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



