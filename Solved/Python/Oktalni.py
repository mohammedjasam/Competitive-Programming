b = input()
ini=b
n=len(b)%3
if n==1:
    b="00"+b
elif n==2:
    b="0"+b
l=[]
i=0
while i <len(b):
    l.append(b[i:i+3])
    i+=3
bToO=['000','001','010','011','100','101','110','111']
ans=""
for x in l:
    ans+=str((bToO.index(x)))
print(ans)
