import sys

t = int(input())

M = 0
S = 0
for i in range(t):
    line = input()
    line = list(map(int, line.split()))
    M = M + line[0]
    S = S + line[1]

M = M * 60
SL = S / M

if SL <= 1:
    print("measurement error")
else:
    print(SL)
