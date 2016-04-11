x2=list()
for i in range(0,1000):
    if(i%4==0 and i%5!=0):
        x2.append(i)
def sumList(list):
    sum=0
    for i in range(0,len(list)):
        sum+=list[i]
    print sum

def lab6():
    sumList(x2)

def main():
    lab6()

if __name__=="__main__":
	main()