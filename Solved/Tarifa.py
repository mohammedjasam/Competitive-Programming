plan = int(input())
used=[]
n = int(input())
m=1
for i in range(n):
    used.append(int(input()))
    m+=1
print((plan*m) - sum(used))
