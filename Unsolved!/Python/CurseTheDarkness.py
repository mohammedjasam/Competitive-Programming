## The whole program is right but it gives a NameError after 1 right testcase! Need help!

import math
tc = int(input())

def checkIfWithin(x,y,x1,y1):
    a1,b1 = (x,y),(x1,y1)
    dist = math.sqrt(sum([(a - b) ** 2 for a, b in zip(a1, b1)]))
    return dist


for i in range(tc):
    ux,uy = map(float, input().split())
    n = int(input())
    for j in range(n):
        candles=[]
        canLight=False
        cx, cy = map(float, input().split())
        candles.append(checkIfWithin(ux,uy,cx,cy))
        for x in candles:
            if x <=8.0:
                canLight=True
                break
    if canLight==True:
        print('light a candle')
    else:
        print('curse the darkness')
