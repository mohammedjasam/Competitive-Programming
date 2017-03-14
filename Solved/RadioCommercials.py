import math
from math import *
n,c=map(int,input().split())

l=[int(x) for x in input().split()]
s=0
for i in range(len(l)):
    l[i]-=c
maxEndingHere,maxSoFar = 0,0
for i in range(n):
    maxEndingHere = max(0, maxEndingHere + l[i])
    maxSoFar = max(maxSoFar, maxEndingHere)
print(maxSoFar)
