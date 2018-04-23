t = int(input())
n = 2
p = 0
for i in range(1, t+1):
    n = n + (n-1)
    p = n*n

print(p)
