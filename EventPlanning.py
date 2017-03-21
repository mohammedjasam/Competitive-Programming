n,budget,h,w = map(int, input().split())
cost=0
f=0
for i in range(h):
    price=int(input())
    seatsAvail=map(int, input().split())
    seatsAvail = sorted(i for i in seatsAvail if i >= n)
    if not seatsAvail:
        pass
    else:
        cost=price*n
    if price*n<=cost:
        cost=price*n
    else:
        f=0
if cost<=budget:
    print(cost)

elif f==0:
    print('stay home')
