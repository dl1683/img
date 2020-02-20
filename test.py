import glob
import os
from txt import *
from sklearn.externals import joblib
from string import ascii_uppercase
def createNew(f1):
    """
    Create a new file storing the good way to store the image details
    """
    file1=open(f1)
    file2=open(r"C:\Users\Devansh\Desktop\Projects\img\test.txt","w+")
    count=0
    text=""
    chars=list(file1.read())
    prevChar=chars[0]
    for i in range(1,len(chars)):
        char=chars[i]
        #print(char,prevChar)
        if(char==prevChar):
            count+=1
        elif(char!=prevChar):
            if(count==1):
                text=text+char
            else:
                text=text+str(count)+char
            prevChar=char
            count=1
    file2.write(text)

def main():
    file1=r"C:\Users\Devansh\Desktop\Projects\img\test2.txt"
    createNew(file1)

#main()

pixel=[0,0,0]

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
        
        print(pred)
        b+=pred[2]
        g+=pred[1]
        r+=pred[0]
        
        i+=1
        
    r=r//(types)
    g=g//(types)
    b=b//(types)
    prediction= [r,g,b ]
    return prediction 



def check():
    neighbors=['T','T','T','T','M','M','A','H','M']
    #colors=colors[:20]
    for index in range(0,len(neighbors),1):
        #TODO: work on the stupid ungraying
        #print("Color:",colors[index])
        neighbors[index]=decodeGrey(neighbors[index])#ungrat
    
    prediction=predict(neighbors)
    print(prediction,neighbors)

def buildList():
    l=[[],[],[],[],[],[]]
    ind=0
    c=list()
    for i in range(6):
        for j in range(18):
            l[i].append(ind)
            c.append(ind)
            ind+=1
    return (l,c)

def a():
    #confirm indexing of my arrays
    load,colors=buildList()
    print(load)
    i,j=2,2
    width=18
    neighbours=[ colors[ width*(i-1) +j],colors[width*(i) +j-1],colors[width*(i-1) +j-1],colors[width*(i) +j],colors[width*(i) +j+1],colors[width*(i+1) +j+1],colors[width*(i+1) +j],colors[width*(i+1) +j-1], colors[width*(i-1) +j+1] ] #list of neighbors
    neighbours2=[ load[i-1][j],load[i][j-1],load[i-1][j-1],load[i][j],load[i][j+1],load[i+1][j+1],load[i+1][j],load[i+1][j-1], load[i-1][j+1] ] #list of neighbors
    #neighbours.sort()
    #neighbours2.sort()
    print(neighbours)
    print(neighbours2)

d=list()
d.append([1,2,3])
a()

        