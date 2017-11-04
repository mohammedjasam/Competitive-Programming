x = input()
x = int(x[:-1])
# print(x)
with open('data.txt') as f:
    count = 0
    for line in f:
        line = line[:-2]
        s = line.split(",")
        s = [int(x) for x in s]
        r,n,l = s[0],s[1],s[2]
        if n == 3:
            if r > ((1.732/4)*l):
                count +=1
            else:
                pass
        elif n == 4:
            
