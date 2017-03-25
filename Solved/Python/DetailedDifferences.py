N = input()
op=[]
A=[]
B=[]
l=[]
ax=""
for i in range(int(N)):
    a=input()
    b=input()
    A.append(a)
    B.append(b)

    for x in range(len(a)):
        if a[x]==b[x]:
            ax+="."
        else:
            ax+="*"
    op.append(ax)
    ax=""

for i in range(len(op)):
    a=""
    print(A[i])
    print(B[i])
    a+=op[i]
    print(a)
