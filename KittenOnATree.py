kpos=int(input())
l=[]
j=[]

j.append(kpos)
def findSub(l):
    for x in (l):
        print(x)
        try:
            if bool(x.index(kpos)):
                j.append(x[0])
        except:
            pass
        j.append(x[0])
        kpos=x[0]
    return j


while True:
    branch=[int(x) for x in input().split()]
    if branch[-1]!=-1:
        l.append(branch)
    else:
        break
sub=0
res=findSub(l)
res=list(set(res))
print(res)
