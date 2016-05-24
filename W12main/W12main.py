import os
def W12main1():
    try:
        mydir=os.getcwd() 
        filename='Python.txt' 
        myfilename=os.path.join(mydir, filename) 
        myfile = open(myfilename,'r')
        contents=myfile.readlines()
        for i in contents:
            if i.find('Python')>=0:
                print i
        myfile.close()
    except IOError as e:
        print e

def lab12():
    W12main1()

def main():
    lab12()

if __name__=="__main__": 
     main()