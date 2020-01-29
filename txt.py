#text processing and testing file
import glob
import numpy as np
from string import ascii_uppercase,ascii_lowercase
from math import pow

#read info from file
#create mapping from range to alphabet
#mapping range --> ranges of 5 [5,15,25,...]:[A,B,C]
#Create actually Encoded file
step=20
stepGrey=0.1
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
    for middle in range (11):
        colorMap[chars[middle]]=float(middle/10)
    print(colorMap)
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
    Take grayscale value and unmap it
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
    Return color value corresponding to the char
    """
    char=str(char).capitalize()
    colorMap=createGreyMap()
    #print(colorMap['A'])
    return( ungray(colorMap[char]) )


def grayScale(n):
    """
    Take pixel and returns the encoded grayscaled value
    """
    r,g,b =n[0]/255, n[1]/255, n[2]/255 #fractional values
    linearCoeff= 0.2126 *r + 0.7152*g + 0.0722*b #math and explaination 
    grayed=0
    if(linearCoeff<=0.0031308): # implementing the gamma adjustement
        grayed= 12.92*linearCoeff
    else:
        grayed=1.055* pow(linearCoeff,1/2.4) - 0.055 #non linear factor
    #return grayed
    return encodeGray(grayed)
    
def ungray(n):
    """
    Take grayscaled n and return ungrayed pixel color
    """
    return int(n*255)

def main():
    #print(encode('255'))
    #print(decode('h'))
    #print(grayScale([125,115,125]))
    for i in range(11):
        print(chars[i],decodeGrey(chars[i]))

if __name__ == "__main__":
    main()

