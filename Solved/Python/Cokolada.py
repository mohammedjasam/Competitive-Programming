# import itertools
# result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == N]'''#Find the sum of elements in a list to a no X'''

import math
from math import *

N=int(input())#5
Smallest = int(math.pow(2,math.ceil(math.log(N)/math.log(2))))
smSq=Smallest
s=0#sum
b=0#stop
while(s < N):
    if Smallest + s <= N:
        s += Smallest
    else:
        b+=1
        Smallest=Smallest//2
print(smSq,b)
