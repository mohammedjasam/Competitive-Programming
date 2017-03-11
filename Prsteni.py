from fractions import Fraction

def run(n):
    s=[int(x) for x in input().split()]
    N=s[0]

    for x in range(n-1):
        st=""
        a=N/s[x+1]
        st=str(Fraction(a))
        if bool(st.count("/")):
            print(st)
        else:
            print(st+"/1")

n=int(input())
if 3<=n<=100:
    run(n)
else:
    pass
