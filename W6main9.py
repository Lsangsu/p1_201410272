def sumOfMultipleOf3_5(begin,end):
    sum=0
    for i in range(begin,end):
        if i%3==0 or i%5==0:
            sum+=i
        elif i%15==0:
            sum-=i          
    return sum
sumOfMultipleOf3_5(1,1000)
