r,c = input().split()
r=int(r)
c=int(c)

rows=[]
for i in range(r):
    a = input()
    rows.append(list(a))

# for i in rows:
    # print(i)

T = [list(i) for i in zip(*rows)]     # Transpose of the matrix
TT = []
# l=[]
for i in T:
    l=[]
    for j in range(len(i)):
        l.append((i[j],j))
    TT.append(l)
# print(TT)

blank = -1
# print(T)

Fin = []
for i in TT:
    for j in i[::-1]:
        if j[0] == '.':
            if blank < j[1]:
                blank = j[1]
        elif j[0] == '#':
            blank = -1
        elif j[0] == 'a':

print(blank)

        # print(j)
        # print()

    # print(i)
