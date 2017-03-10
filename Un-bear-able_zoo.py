for i in range(5):
    n=int(input())
    if n==0:
        break
    l=[]
    for x in range(n):
        s=input()
        l.append(s.lower())
    a=[]
    ax=[]
    for word in (l):
        z=word.split()[-1]
        a.append(z)
        ax.append((word.split()[-1],1))
        axx=[]
        for word in ax:
            axx.append((word[0],ax.count(word)))

        axx=list(set(axx))
    print("List "+str(i+1)+":")
    axx.sort()
    for i in range(len(axx)):
        print(axx[i][0]+" | "+ str(axx[i][1]))
