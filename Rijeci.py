table = {}
def fibRec(n):
    if n in table:
        return table[n]
    else:
        table[n] = n if n < 2 else fibRec(n-2) + fibRec(n-1)
        return table[n]

N = int(input())
numA = fibRec(N -1)
numB = fibRec(N)
print("%d %d" %(numA,numB))
