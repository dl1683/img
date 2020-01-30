
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
def stringify(pixel):
    return (float(str(pixel[0])+str(pixel[1])+str(pixel[2])))

def isValidDecomp(num,decmp,left):
    print("Sending",num[pos:pos+length],"for params num:",num,"lenght:",length,"pos: ",pos )
    if(len(num)-len(decmp)>=left):
        if(int(decmp)<256):
            return True
    return False

def splitter(s):
    for i in range(1, len(s)):
        start = s[0:i]
        end = s[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield tuple(result)

def getDecomps(s):
    return [x for x in splitter(s) if len(x) == 3 and all((len(y) <= 3 ) for y in x)]

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

d=average('[26330333.4178834]')
print(d)


        