#Get everything
from sklearn.externals import joblib
import glob
import cv2
import numpy as np
from txt import * 
from sklearn import svm,linear_model,tree
from tkinter import filedialog
from tkinter import *
from sklearn import neural_network,ensemble,gaussian_process
from sklearn import isotonic, neighbors, multioutput



def getNames():
    for i in trainers:
        names.append(str(i))
    return names

def getTrainers():
    return trainers

def trainData(dir):
    """
    Using all the files in dir, train the data 
    """
    dir=dir+r"/pics/"
    print(dir)
    imgList=glob.glob(dir+r"*.jpg")
    imgList.extend(glob.glob(dir+r"*.jpeg"))
    imgList.extend(glob.glob(dir+r"*.png"))
    imgList.extend(glob.glob(dir+r"*.jfif"))
    dumpingGround= filedialog.askdirectory(parent=root,initialdir="/",title='Please select a dumping ground')
    #dumpingGround=r"/home/stu2/s15/dl1683/Courses/img/TrainedData"
    for img in imgList:
        processImg(img,dumpingGround)
        print("Moved imgs")
    
    for i in range (0,len(trainers)):
        multioutput.MultiOutputRegressor(clfB[i]).fit(x,pixels)
        print("Fitting blue")
        print("Dumping",names[i])
        joblib.dump(clfR[i],dumpingGround+r"/trainRed"+(names[i])[:10] )
        joblib.dump(clfB[i],dumpingGround+r"/trainBlue"+(names[i])[:10])
        joblib.dump(clfG[i],dumpingGround+r"/trainGreen"+(names[i])[:10])

def processImg(img,dumpingGround):
    load=cv2.imread(img)
    height, width, layers = load.shape

    #print(height,width, layers)
    for i in range(1,height-1):
        for j in range(1,width-1):
            print("Moved pixels",i,j)
            #sPixel.append( int(str(pixel[0])+str(pixel[1])+str(pixel[2])) )
            neighbours=[ load[i-1,j],load[i,j-1],load[i-1,j-1],load[i,j],load[i,j+1],load[i+1,j+1],load[i+1,j],load[i+1,j-1], load[i-1,j+1] ] #list of neighbors
            #get 3 seperate
            gray=list()
            
            for pixel in neighbours:
                #text=text+(encode(str(pixel[0]))+encode(str(pixel[1]))+encode(str(pixel[2]))) #text           
                gray.append(grayScale(pixel))
            
            x.append(gray)
            pixels.append(load[i,j])
                #print("Fitting:",x,sPixel)
                #file1.write('\n')
    return (height,width)


trainers=[gaussian_process.GaussianProcessRegressor(),linear_model.LinearRegression(),neural_network.MLPRegressor(),neighbors.KNeighborsRegressor()]
names=list()
names=getNames()
clfR = trainers.copy()
clfB = trainers.copy()
clfG=trainers
pixels=list()
x=list()

root = Tk()
dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select the image directory')
trainData(dirname)
