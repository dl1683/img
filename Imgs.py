import glob
import numpy as np
from txt import * 
from sklearn.externals import joblib
import os
from PIL import Image as img
import math,random 
import cv2 #didn't want to go through the trouble of redoing this a 100 times. 

#global gamma
gamma=0

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
    global gamma
    r,g,b=0,0,0
    trainers=list(os.listdir(r"C:\Users\Devansh\Desktop\Projects\img\TrainedData"))
    d=r"C:\Users\Devansh\Desktop\Projects\img\TrainedData"
    l=len(trainers)
    i=0
    types=len(trainers)
    x=[gr]
    pred=list()
    while(i< types ):
        t=d+"/"+ trainers[i]
        clf = joblib.load(t)
        pred=clf.predict(x)[0]
        
        b+=pred[2]/types
        g+=pred[1]/types
        r+=pred[0]/types
        
    

        i+=1
    #by adjusting the values and scaling them, we can reduce the effects of overfitting. 
    gamma+=((0.2126 * r + 0.7152 * g + 0.0722 * b)/255) *(random.randrange(-300000,300000)/30000) #optimize (range will give a -10<val<10)
    print(gamma)
    
    if gamma>=0:
        r=(random.randrange(int((r-gamma-1)),int(r+gamma)+1 ))
        g=(random.randrange((int(g-gamma-1)),int(g+gamma)+1 ))
        b=(random.randrange((int(b-gamma-1)),int(b+gamma)+1 ))
    else:
        r=(random.randrange(int((r+gamma-1)),int(r-gamma)+1 ))
        g=(random.randrange((int(g+gamma-1)),int(g-gamma)+1 ))
        b=(random.randrange((int(b+gamma-1)),int(b-gamma)+1 ))
        """
    print("Created: ",r,g,b)
    correction=(.2126*random.randrange(0,int(r)+1)+.7152*random.randrange(0,int(g)+1)+0.722*random.randrange(0,int(b)+1))
    print(correction)
    
    #to use when I start testing and building my model with error calculations
    r=(random.randrange(abs(int(r-2*correction)),int(r+1+2*correction)))/(types)
    g=(random.randrange(abs(int(g-2*correction)),int(g+1+2*correction)))/(types)
    b=(random.randrange(abs(int(b-2*correction)),int(b+1+2*correction)))/(types)
    
    prediction= [r,g,b ]
    print("Weighed", r,g,b)
    """
    prediction=[r,g,b]
    
    for i in range (len(prediction)):
        if(prediction[i]>255):
            prediction[i]%=255 #build equivalence classes for predictions
        elif(prediction[i]<0):
            prediction[i]*=-1
            if(prediction[i]>255):
                prediction[i]%=255 #build equivalence classes for predictions
        gamma+=(prediction[i]-pred[i])**2
    gamma%=math.sqrt(abs(gamma)) #self correction with gamma
    return prediction 

def blackAndWhite(height,width,name,ext):
    """
    Create the grayScale image with the file
    """
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt")
    blank_image = np.zeros((height,width,3), np.uint8)
    i=0 #height index
    j=0 #width index
    colors=list(file1.read())
    for index in range(0,len(colors),1):
        

        """
        r=decode(colors[index])
        g=decode(colors[index+1])
        b=decode(colors[index+2])
        prediction=[r,g,b]
        """
        ga=decodeGrey(colors[index])*255
        print(colors[index],ga)
        blank_image[i][j]=[ga,ga,ga]
        
        if ( j<width-1 ):
            j+=1
            
        else:
            j=0
            i+=1
            
    cv2.imwrite("BlackAndWhite"+name+ext,blank_image)
    cv2.destroyAllWindows()



def convertToImg(height,width,name,ext):
    file1=open(r"C:\Users\Devansh\Desktop\Projects\img\test2.txt")
    blank_image = np.zeros((height,width,3), np.uint8)
    i=1 #height index
    j=1 #width index
    colors=list(file1.read())
    for index in range(width,len(colors)-width-2,1):
        
        #print(i,j,len(colors),index,width)
        
        neighbours=[ colors[ width*(i-1) +j],colors[width*(i) +j-1],colors[width*(i-1) +j-1],colors[width*(i) +j],colors[width*(i) +j+1],colors[width*(i+1) +j+1],colors[width*(i+1) +j],colors[width*(i+1) +j-1], colors[width*(i-1) +j+1] ] #list of neighbors
        
        for index in range(0,len(neighbours),1):
            neighbours[index]=decodeGrey(neighbours[index])#ungray
        
        prediction=predict(neighbours)
        print("pred",prediction)

        blank_image[i][j]=prediction
        
        if ( j<width-1 ):
            j+=1
            
        else:
            j=0 #skip the first column
            i+=1
            
    cv2.imshow("Get Wrecked Shree", blank_image)
    cv2.waitKey(0)
    cv2.imwrite("tested"+name+ext,blank_image)
    cv2.destroyAllWindows()

