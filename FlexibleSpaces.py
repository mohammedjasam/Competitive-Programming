w,p=map(int, input().split())
rm=[]
room={}
for i in range(w+1):
    rm.append(0)
    room[i]=0
pars=[int(x) for x in input().split()]
l=[]
for i in pars:
    rm[i]=1
for i in range(w+1):
    for j in pars:
        if not((abs(i-j))>w or (abs(i+j))>w):
            l.append(abs((i)-(j)))
            l.append(abs((i)+(j)))


l=list(set(l))
l.sort()
if l.count(0)==1:
    l.remove(0)
s=""
for x in l:
    s+=str(x)+" "
print(s[:-1])
