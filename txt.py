#text processing and testing file
import glob
import numpy as np
from string import ascii_uppercase,ascii_lowercase
from math import pow
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

#read info from file
#create mapping from range to alphabet
#mapping range --> ranges of 5 [5,15,25,...]:[A,B,C]
#Create actually Encoded file
step=20
stepGrey=0.05
colorMap=dict()
chars=list(ascii_uppercase)

def createMap():
    
    i=0
    for middle in range (0,256,step):
        colorMap[chars[i]]=middle
        i+=1
    #print(colorMap)
    return colorMap

def createGreyMap():
    for middle in range (21):
        g=float(middle/20)
        ga=ungray(g)
        #print(chars[i],g,ga,grayScale([ga,ga,ga]))
        colorMap[chars[middle]]=grayScale([ga,ga,ga])

    #print(colorMap)
    return colorMap


def encode(color):
    """
    Encode the pixels color into the map
    """
    color=int(color)
    colorMap=createMap() #get the mapping for pixel value to letter
    alpha=color//step #the alphabet corresponding to the number
    return(str(list(colorMap.keys())[alpha]))

def encodeGray(grayed):
    """
    Take grayscale value and map it to our charset
    """
    colorMap=createGreyMap()
    alpha=int(grayed/stepGrey) #the alphabet corresponding to the number
    return(str(list(colorMap.keys())[alpha]))


def decode(char):
    """
    Return color value corresponding to the char
    """
    char=str(char).capitalize()
    colorMap=createMap()
    #print(colorMap['A'])
    return(int(colorMap[char]))

def decodeGrey(char):
    """
    Return color value corresponding to the char for grey map
    """
    char=str(char).capitalize()
    colorMap=createGreyMap()
    #print(colorMap['A'])
    return( float(colorMap[char]) )


def grayScale(n):
    """
    Take pixel and returns the mathematical grayscaled value
    """
    r,g,b =n[0]/255, n[1]/255, n[2]/255 #fractional values
    linearCoeff= (0.2126 * r + 0.7152 * g + 0.0722 * b) #math and explaination in documentation
    grayed=0
    if(linearCoeff<=0.0031308): # implementing the gamma adjustement
        grayed= 12.92*linearCoeff
    else:
        grayed=1.055* pow(linearCoeff,1/2.4) - 0.055 #non linear factor
    #return grayed
    return grayed
    
def ungray(n):
    """
    Take grayscaled n and return ungrayed pixel color
    """
    #TODO: find the actual probability distribution.
    return int(n*255)

def main():
    #print(encode('255'))
    #print(decode('h'))
    #print(grayScale([125,115,125]))
    for i in range(21):
        g=decodeGrey(chars[i])
        ga=ungray(g)
        print(chars[i],g,ga,grayScale([ga,ga,ga]))
    print(colorMap)

if __name__ == "__main__":
    main()

def stringify(pixel):
    return (int(str(pixel[0])+str(pixel[1])+str(pixel[2])))

def isValidDecomp(num,decmp,left):
    """
    Possible checker for this stuff
    """
    #print("Sending",num[pos:pos+length],"for params num:",num,"lenght:",length,"pos: ",pos )
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
    #print(decomps)
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
    #l.sort()
    for char in s:
        if not (char.isdigit()) :
            l.remove(char)
    new=""
    for char in l:
        new=new+str(char)
    
    if(len(new)>9):
        new=new[0:9]
    #print(l,new)
    return new
