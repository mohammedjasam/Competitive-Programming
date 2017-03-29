n = int(input())

for i in range(n):
    s=[int(x) for x in (input())]
    maxi=0
    s=list(s)
    for x in range(len(s)):
        jx=""
        for j in range(0,x+1):
            jx+=str(s[j])
            b=bin(int(jx))
            b=list(b)
            del b[0]
            del b[0]
            curr=b.count('1')
            if curr>maxi:
                maxi=curr
    print(maxi)
