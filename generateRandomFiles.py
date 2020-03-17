import random
import string

def generateRandom (inputlen):
    randomOut = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(inputlen)])
    return randomOut

def writeFile (fileName,inputLength):
    name = fileName
    file = open(name,"w+")
    file.write(generateRandom(inputLength))

def main():
    fileSize = 1024*1024*20
    howManyFiles = 50
    x = 1
    while x < howManyFiles :
        writeFile(str(x),fileSize)
        x = x+1

if __name__== "__main__":
  main()
