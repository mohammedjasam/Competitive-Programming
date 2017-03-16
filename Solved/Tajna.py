# from functools import reduce
import math
# from math import*
def factors(n):
    return [x for x in range(1, n+1) if n % x == 0]
s=input()
n= len(s)
# n = int(input())
a=list(factors(n))
# print(a)


a.sort()
i=0
j=len(a)
r=[]
c=[]
maxr=0
maxc=0
if len(a)%2!=0:
    z=a[int(len(a)/2)]
    r.append(z)
    c.append(z)
    maxr,maxc=z,z
else:
    for i in a:
        for j in a:
            if i*j==n:
                r.append(i)
                c.append(j)

if len(a)%2==0:
    for i in range(int(len(r)/2)):
        for j in range(int(len(r)/2)):
            maxr=r[i]
            maxc=c[j]
s=list(s)
d=s
# import numpy as np
whaL=[]
for j in range(1,maxc+1):
    for i in range(1,maxr+1):
        s1=int(str(i)+str(j))
        whaL.append((s1,d[0]))
        del d[0]
string=""
for i in range(1,maxr+1):
    for j in range(1,maxc+1):

        s1=int(str(i)+str(j))
        whaL=dict(whaL) ### Finds within a list of tups
        string+=whaL[s1] ### appending the answer to the string
print(string)
