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


def lab8():
    charCount()

def main():
    lab8()
    

if __name__=="__main__":
    main()