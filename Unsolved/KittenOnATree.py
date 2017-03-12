kpos=int(input())
l=[]
j=[]
j.append(kpos)

def findSub(l,kpos):
    for i in range(len(l)):
        for x in (l):
            if x.count(kpos)==1:
                kpos=x[0]
                j.append(kpos)
            else:
                continue
    return j

while True:
    branch=[int(x) for x in input().split()]
    if branch[-1]!=-1:
        l.append(branch)
    else:
        break
res=findSub(l,kpos)
res=list(set(res))
result=""
for x in (res):
    result+=str(x)+" "

print(result)
