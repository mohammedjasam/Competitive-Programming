import sys
for line in sys.stdin:
    a,b=line.split(' ')
    a=int(a)
    b=int(b)
    print(abs(a-b))
