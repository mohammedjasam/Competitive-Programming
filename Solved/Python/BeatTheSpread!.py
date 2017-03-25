n = int(input())
for i in range(n):
    a,b = map(int, input().split())

    x=(a+b)//2
    y=(a-((a+b)//2))
    if not(b>a or ((a+b)%2!=0)):
        # print((a+b)//2,(a-((a+b)//2)))
        print(x,y)
    else:
        print("impossible")
