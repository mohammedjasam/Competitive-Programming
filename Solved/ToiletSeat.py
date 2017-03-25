s = input()
s=list(s)
u,d,o=0,0,0

#Policy 1
state=s[0]
for i in range(1,len(s)):
    if state=='D':
        u+=1
    else:
        if s[i]=='D':
            u+=2
    state = 'U'
print(u)

#Policy 2
state=s[0]
for i in range(1,len(s)):
    if state=='D':
        # d+=1
        if s[i]=='U':
            d+=2
    else:
        d+=1
    state='D'
print(d)

#Policy 3
state=s[0]
for i in range(1,len(s)):
    if state=='D':
        if s[i]=='U':
            o+=1
    else:
        if s[i]=='D':
            o+=1
    state=s[i]

print(o)
