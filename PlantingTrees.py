n= int(input())
l= [int(x) for x in input().split()]
l.sort()
answer = 0
for i in range(n):
    if (l[i]+n-i > answer):
        answer = l[i]+n-i;
print(str(answer + 1))
