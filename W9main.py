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
    

def lab9():
    charCount()
    countDigitsLetters()

def main():
    lab9()
    

if __name__=="__main__":
    main()
