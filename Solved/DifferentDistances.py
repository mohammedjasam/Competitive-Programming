import sys
for i in range(1000):
    try:
        x1,y1,x2,y2,p=map(float,input().split())

        x1=float(x1)
        y1=float(y1)
        x2=float(x2)
        y2=float(y2)
        p=float(p)
        norm=((((x1-x2)**p)+((y1-y2)**p))**(1/p))
        print(abs(norm))
    except:
        sys.exit()
