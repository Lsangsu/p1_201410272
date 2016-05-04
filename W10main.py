def distance():
    Locations=list()
    Locations=[(37.576484, 126.985447),(37.574480, 126.957821),(37.571516, 126.976580),(37.570182, 126.983029),(37.563565, 126.975394)]
    import math
    d=list()
    for i in range(0,len(Locations)):
        d.append(math.sqrt((37.575883-Locations[i][0])**2 + (126.973480-Locations[i][1])**2))
    print d
    print min(d)

def lab10():
    distance()

def main():
    lab10()
    

if __name__=="__main__":
    main()
