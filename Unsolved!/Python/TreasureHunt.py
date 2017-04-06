import numpy as np

r, c = map(int, input().split())
arr=[]
for i in range(r):
    s= input()
    s=list(s)
    arr.append(s)

print(arr[0][0])
