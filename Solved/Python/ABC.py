s=[int(x) for x in input().split()]
s.sort()

op=input()
st=""
for i in range(len(s)):
    if op[i]=='A':
        st+=str(s[0])+" "
    elif op[i]=='B':
        st+=str(s[1])+" "
    elif op[i]=='C':
        st+=str(s[2])+ " "

print(st[:-1])
j=st[:1]
print(j)
