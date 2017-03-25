import sys
names=[]
for line in sys.stdin:
    try:
        f,l=line.split(' ')
        names.append((f,l[:-1]))
    except:
        print(names)
