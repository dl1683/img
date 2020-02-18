import glob
import numpy as np
from txt import * 
from sklearn.externals import joblib
import os
from PIL import Image as img
import math 
import cv2 #didn't want to go through the trouble of redoing this a 100 times. 

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
            #sPixel.append( int(str(pixel[0])+str(pixel[1])+str(pixel[2])) )
            
            
            #text=text+(encode(str(pixel[0]))+encode(str(pixel[1]))+encode(str(pixel[2]))) #text
            
            grayed=grayScale(pixel)
            
            text=text+ str( encodeGray(grayed))
            #file1.write('\n')
    
    
    
    file1.write(text)

    return (height,width)

def downsample(img):
    """
    Take the information from the imgFile and downsample the image accordingly
    @return the scaled down image dimensions
    """
    load=cv2.imread(img)
    height, width, layers = load.shape
    text=""
    #print(height,width, layers)
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\downsampled.txt","w+")
    
    for i in range(height-1):
        for j in range(width-1): #avoid the rightmost places 
            neighbours=[ load[i,j],load[i,j+1],load[i+1,j+1],load[i+1,j] ] #list of neighbors
            pixel=[0,0,0]
            for idx in range(4): #neighbors
                for pxl in range(3): #r,g,b
                    pixel[pxl]+=neighbours[idx][pxl]
            #sPixel.append( int(str(pixel[0])+str(pixel[1])+str(pixel[2])) )
            
            
            text=text+(encode(str(pixel[0]))+encode(str(pixel[1]))+encode(str(pixel[2]))) #text
            
            #grayed=grayScale(pixel)
            
            #text=text+ str( encodeGray(grayed))
            #file1.write('\n')
    
    
    
    file1.write(text)

    return (height,width)


def predict(gr):
    """
    Weight all the neural nets and work it out
    @param: ungrayed pixel
    @return: the averaged vals
    """
    r,g,b=0,0,0
    trainers=list(os.listdir(r"C:\Users\Devansh\Desktop\Projects\img\TrainedData"))
    d=r"C:\Users\Devansh\Desktop\Projects\img\TrainedData"
    l=len(trainers)
    i=0
    types=l

    x=[gr]
    while(i< types ):
        t=d+"/"+ trainers[i]
        clf = joblib.load(t)
        pred=clf.predict(x)[0]
        
        b+=pred[2]
        g+=pred[1]
        r+=pred[0]
        
        i+=1
        
    r=abs(r)//(types)
    g=abs(g)//(types)
    b=abs(b)//(types)
    prediction= [r,g,b ]
    return prediction 

def processImg(img,ext):
    load=cv2.imread(img)
    height, width, layers = load.shape
    blank_image = np.zeros((height,width,3), np.uint8)
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt")
    colors=list(file1.read())

    #print(height,width, layers)
    for i in range(1,height-1):
        for j in range(1,width-1):
            #print("Moved pixels",i,j)
            #sPixel.append( int(str(pixel[0])+str(pixel[1])+str(pixel[2])) )
            neighbours=[ load[i-1,j],load[i,j-1],load[i-1,j-1],load[i,j],load[i,j+1],load[i+1,j+1],load[i+1,j],load[i+1,j-1], load[i-1,j+1] ] #list of neighbors
            #get 3 seperate
            gray=list()
            
            for pixel in neighbours:
                #text=text+(encode(str(pixel[0]))+encode(str(pixel[1]))+encode(str(pixel[2]))) #text           
                gray.append(grayScale(pixel))
            
            prediction=predict(gray)
            print(prediction)
            blank_image[i][j]=prediction

            
                #print("Fitting:",x,sPixel)
                #file1.write('\n')
    
    cv2.imshow("Get Wrecked Shree", blank_image)
    cv2.waitKey(0)
    cv2.imwrite("tested"+ext,blank_image)
    cv2.destroyAllWindows()

    return (height,width)



def convertToImg(height,width,ext):
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt")
    blank_image = np.zeros((height,width,3), np.uint8)
    i=1 #height index
    j=1 #width index
    colors=list(file1.read())
    for index in range(width,len(colors)-width-2,1):
        #TODO: work on the stupid ungraying
        #print("Color:",colors[index])
        #prediction=predict(decodeGrey(colors[index]))
        print(i,j,len(colors),width,index)
        neighbours=[ colors[ width*(i-1) +j],colors[width*(i) +j-1],colors[width*(i-1) +j-1],colors[width*(i) +j],colors[width*(i) +j+1],colors[width*(i+1) +j+1],colors[width*(i+1) +j],colors[width*(i+1) +j-1], colors[width*(i-1) +j+1] ] #list of neighbors
        print(neighbours)
        for index in range(0,len(neighbours),1):
        #TODO: work on the stupid ungraying
        #print("Color:",colors[index])
            neighbours[index]=decodeGrey(neighbours[index])#ungray
        
        prediction=predict(neighbours)
        print(prediction)

        """
        r=decode(colors[index])
        g=decode(colors[index+1])
        b=decode(colors[index+2])
        prediction=[r,g,b]
        """
        blank_image[i][j]=prediction
        
        if ( j<width-1 ):
            j+=1
            
        else:
            j=0
            i+=1
            
    cv2.imshow("Get Wrecked Shree", blank_image)
    cv2.waitKey(0)
    cv2.imwrite("tested"+ext,blank_image)
    cv2.destroyAllWindows()

