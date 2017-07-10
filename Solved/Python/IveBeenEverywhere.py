tc = int(input())
for i in range(tc):
    t = int(input())
    l=[]
    for j in range(t):
        a = input()
        if a not in l:
            l.append(a)
        else:
            pass
    print(len(l))
