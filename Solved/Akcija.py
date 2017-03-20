n = int(input())
l=[]

for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
# print(l)

sum=0

for x in range(len(l)):
    if (x+1)%3==0:
        # print(x)
        pass
    else:
        sum+=l[x]

print(sum)
