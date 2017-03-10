testcases=int(input())
days1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
days2=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
days3=['Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']
days4=['Wednesday','Thursday','Friday','Saturday','Sunday','Monday','Tuesday']
days5=['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']
days6=['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
days7=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
for i in range(testcases):
    D,M=map(int, input().split())
    d=[int(x) for x in input().split()]
    l=[]
    days=days1
    for x in d:
        for z in range(x):
            l.append((z+1,days[(z)%7]))
        # print(l[-1][1])
        if (l[-1][1])=="Sunday":
            days=days2
        elif (l[-1][1])=="Monday":
            days=days3
        elif (l[-1][1])=="Tuesday":
            days=days4
        elif (l[-1][1])=="Wednesday":
            days=days5
        elif (l[-1][1])=="Thursday":
            days=days6
        elif (l[-1][1])=="Friday":
            days=days7
        else:
            days=days1
    print(l.count((13,'Friday')))
