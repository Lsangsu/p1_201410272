def charCount():
    word=raw_input('Enter the word~')
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    print word
    print d

def countDigitsLetters():
    word=raw_input('Enter the word~')
    d=dict()
    d['number']=0
    d['text']=0
    for c in word:
        if c.isdigit():
            d['number']+=1
        else:
            d['text']+=1
    print d
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(d)), d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()
    
def distance():
    Locations=list()
    Locations=[(37.576484, 126.985447),(37.574480, 126.957821),(37.571516, 126.976580),(37.570182, 126.983029),(37.563565, 126.975394)]
    import math
    d=list()
    for i in range(0,len(Locations)):
        d.append(math.sqrt((37.575883-Locations[i][0])**2 + (126.973480-Locations[i][1])**2))
    print d
    print min(d)

def lab8():
    charCount()
    countDigitsLetters()
    distance()

def main():
    lab8()
    

if __name__=="__main__":
    main()
