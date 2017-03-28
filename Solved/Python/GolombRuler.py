import sys
d={}
for line in sys.stdin:
    for i in range(1,2001):
        d[i]=0
    s=line[:-1]
    s=[int(x) for x in s.split()]
    lol=[]
    s.sort()
    for li in range(s[-1]+1):
        lol.append(li)
    rofl=lol
    del lol[0]
    c=len(s)
    forms=[]
    for i in range(len(s)):
        for j in range(len(s)):
            val=s[j]-s[i]
            if val in d:
                forms.append(val)
                d[val]+=1
    okay=1
    fin=list(set(forms))
    if len(fin)==len(lol):
        for x in fin:
            if d[x]==1:
                pass
            else:
                okay=0
                break
        if okay==0:
            print("not a ruler")
        else:
            print("perfect")
    else:
        for x in fin:
            if d[x]==1:
                pass
            else:
                okay=0
                break
        if okay==0:
            print("not a ruler")
        else:
            for jas in fin:
                lol.remove(jas)
            res=""
            for x in lol:
                res+=" " +str(x)
            print("missing"+res)
