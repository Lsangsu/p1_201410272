def distance():
    Locations=list()
    Locations=[(37.576484, 126.985447),(37.574480, 126.957821),(37.571516, 126.976580),(37.570182, 126.983029),(37.563565, 126.975394)]
    import math
    d=list()
    for i in range(0,len(Locations)):
        d.append(math.sqrt((37.575883-Locations[i][0])**2 + (126.973480-Locations[i][1])**2))
    print d
    print min(d)

def popSumG():
    pop=[[74425, 76326],
    [61164, 61636],
    [109688, 115744],
    [144796, 146776],
    [174996, 181676],
    [177841, 177434],
    [204630, 205980],
    [223373, 232245],
    [161055, 166130],
    [171576, 176735],
    [279169, 293772],
    [239450, 251066],
    [148690, 156510],
    [182977, 196992],
    [237792, 242641],
    [283869, 296762],
    [209344, 210282],
    [118965, 114441],
    [186503, 186856],
    [195734, 203014],
    [254381, 249472],
    [212401, 229111],
    [271654, 295354],
    [319197, 335045],
    [229829, 231671]]
    malesum=0
    femalesum=0
    for i in pop:
        malesum+=i[0]
        femalesum+=i[1]
    print 'Sum of male: ', malesum,' Average of male: ', malesum/len(pop)
    print 'Sum on female: ', femalesum,' Average of female: ', femalesum/len(pop)
    popSum=list()
    for i in pop:
        popSum.append(i[0]+i[1])
    print popSum
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(popSum)), popSum,align='center')
    plt.show()
    
def lab10():
    distance()
    popSumG()

def main():
    lab10()
    

if __name__=="__main__":
    main()
