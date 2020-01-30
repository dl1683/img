import glob
import cv2
import numpy as np
from txt import * 
from new_net import *
from sklearn import svm,linear_model

clf = linear_model.BayesianRidge()
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
    x=list()
    sPixel=list()
    for i in range(height):
        for j in range(width):
            pixel=load[i,j]
            sPixel.append( int(str(pixel[0])+str(pixel[1])+str(pixel[2])) )
            #text=text+(encode(str(pixel[0]))+encode(str(pixel[1]))+encode(str(pixel[2]))) #text
            grayed=grayScale(pixel)
            x.append([0,grayed])
            #print("Fitting:",x,sPixel)
            text=text+ str( encodeGray(grayed))
            #file1.write('\n')
    clf.fit(x,sPixel)
    file1.write(text)

    return (height,width)

def convertToImg(height,width):
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt")
    blank_image = np.zeros((height,width,3), np.uint8)
    i=0 #height index
    j=0 #width index
    colors=list(file1.read())
    for index in range(0,len(colors),1):
        #TODO: work on the stupid ungraying
        #print("Color:",colors[index])
        x=[[0,decode(colors[index])]]
        prediction=(clf.predict(x))
        if(prediction==0):
            blank_image[i][j]=[0,0,0]
        else:
            predictionS=str(prediction)
            #index=
            pixelAvg=average(predictionS)
            blank_image[i][j]=[int(pixelAvg[0]),int(pixelAvg[1]),int(pixelAvg[2])]
        #print("Pixel: ",pixelAvg)
        #blank_image[i][j]=[int(decode(colors[index])),int(decode(colors[index+1])),int(decode(colors[index+2]))]
        if ( j<width-1 ):
            j+=1
        else:
            j=0
            i+=1
    cv2.imshow("Get Wrecked Shree", blank_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def stringify(pixel):
    return (int(str(pixel[0])+str(pixel[1])+str(pixel[2])))

def isValidDecomp(num,decmp,left):
    """
    Possible checker for this stuff
    """
    print("Sending",num[pos:pos+length],"for params num:",num,"lenght:",length,"pos: ",pos )
    if(len(num)-len(decmp)>=left):
        if(int(decmp)<256):
            return True
    return False

def splitter(s):
    """
    Split substring into all possible substrings of the number
    """
    for i in range(1, len(s)):
        start = s[0:i]
        end = s[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield tuple(result)

def getDecomps(s):
    """
    Make sure the lists returned are in acceptable boundaries
    """
    return [x for x in splitter(s) if len(x) == 3 and all(len(y) <= 3 for y in x)]

def average(num):
    """
    Given a string containing possible RGB vals, create an average value distribution
    """
    colors=[0,0,0]#default
    num=clean(num)
    decomps=getDecomps(str(int(num)))
    print(decomps)
    for i in range(3): #r,g,b
        count=0
        for y in decomps:
            colors[i]+=int(y[i])
            count+=1
        colors[i]=colors[i]//count
        if(colors[i]>255):
            colors[i]=255
    return colors

def clean(num):
    """
    Purge the stupid string num of any evil
    """
    s=str(num)
    l=list(s)
    for char in s:
        if not (char.isdigit()) :
            l.remove(char)
    new=""
    for char in l:
        new=new+str(char)
    
    if(len(new)>9):
        new=new[0:9]
    print(l,new)
    return new
