kpos=int(input())

r=[]
r.append(kpos)
def findRoot(x):
    try:
        path=d[x]
        r.append(path)
        findRoot(path)
    except:
        s=""
        for j in r:
            s+=str(j)+ " "
        print(s[:-1])
d={}
while 1:
    x= [int(x) for x in input().split()]
    if x[0]==-1:
        break
    else:
        root=x[0]
        del x[0]
        for i,a in enumerate(x):
            pass
            d[a]=root
d=dict(sorted(d.items()))
findRoot(kpos)
