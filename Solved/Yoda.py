a = input()
b = input()

a=[int(x) for x in a]
b=[int(x) for x in b]

if len(a)<len(b):
    while(len(a)<len(b)):
        a=[0]+a

elif len(b)<len(a):
    while(len(b)<len(a)):
        b=[0]+b
# print("\nmade into same length")
# print(a)
# print(b)
a.reverse()
b.reverse()
# print("\nmade into reverse")
# print(a)
# print(b)
revstrA=""
revstrB=""
for i in range(max(len(a),len(b))):
    # try:
    if a[i]==b[i]:
        revstrA+=str(a[i])
        revstrB+=str(b[i])
    elif a[i]>b[i]:
        revstrA+=str(a[i])
    elif a[i]<b[i]:
        revstrB+=str(b[i])
    # except:


fina=[int(x) for x in revstrA]
finb=[int(x) for x in revstrB]
finalA,finalB="",""
# print("\nReverse str")
# print(fina)
# print(finb)
fina.reverse()
finb.reverse()

for i in fina:
    finalA+=str(i)
for i in finb:
    finalB+=str(i)
# print("\nfinal result")
if not finalA:
    print("YODA")
    print(int(finalB))
elif not finalB:
    print(int(finalA))
    print("YODA")
else:
    print(int(finalA))
    print(int(finalB))
