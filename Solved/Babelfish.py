d={}
while 1:
    s=input()
    if s=='':
        break
    a,b=s.split(' ')
    d[b]=a

while 1:
    try:
        s=input().rstrip('\n')
    except:
        break
    print(d.get(s,'eh'))
