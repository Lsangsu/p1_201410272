def FindLeapYear(year):
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        res="LeapYear!!"
    else:
        res="Normal Year"
    return res

FindLeapYear(2016)

def lab6():
    FindLeapYear(2016)

def main():
    lab6()

if __name__=="__main__":
    main()
