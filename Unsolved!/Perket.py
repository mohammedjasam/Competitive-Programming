n = int(input())
prod=1
s=0
eAns=0
for i in range(n):
    print('prod is: '+str(prod),'sum is: '+str(s))
    x,y=map(int,input().split())
    prod*=x
    s=s+y
    ans=abs(prod-s)
    if i>0:
        if eAns<ans:
            print(eAns)
            break
        else:
            eAns=ans
        print(abs(prod-s))
