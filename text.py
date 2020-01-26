#text processing and testing file
import glob
import numpy as np
from string import ascii_uppercase,ascii_lowercase

#read info from file
#create mapping from range to alphabet
#mapping range --> ranges of 5 [5,15,25,...]:[A,B,C]
#Create actually Encoded file

def createMap():
    colorMap=dict()
    chars=list(ascii_uppercase)
    i=0
    for middle in range (5,260,10):
        colorMap[chars[i]]=middle
        i+=1
    print(colorMap)
    return colorMap

def encode(color):
    """
    Encode the pixels color into the map
    """
    colorMap=createMap() #get the mapping for pixel value to letter
    alpha=color//10 #the alphabet corresponding to the number
    print(colorMap.keys[alpha])

def main():
    encode(18)

if __name__ == "__main__":
    main()
