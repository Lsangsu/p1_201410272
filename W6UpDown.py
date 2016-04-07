def UpDown(FindNum,ThinkNum):
        if FindNum>ThinkNum:
            print "UP!!"
        elif  FindNum<ThinkNum:
            print "DOWN!!"
        elif FindNum==ThinkNum:
            print "Correct"

def lab6():
    FindNum=raw_input("Set Number!!")
    ThinkNum=raw_input("FInd Number~ ")
    UpDown(FindNum,ThinkNum)

def main():
    lab6()

if __name__=="__main__":
    main()