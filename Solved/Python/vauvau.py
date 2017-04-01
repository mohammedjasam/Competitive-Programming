dog1, dog1_peace, dog2, dog2_peace=map(int, input().split())
postman, milkman,garbageman=map(int, input().split())

d1=[]
d2=[]
for i in range(1000):
    for x in range(dog1):
        d1.append('a')
    for x in range(dog1_peace):
        d1.append('c')
    for x in range(dog2):
        d2.append('a')
    for x in range(dog2_peace):
        d2.append('c')

if d1[postman - 1]=='a' and d2[postman - 1]=='a':
    print('both')
elif (d1[postman - 1]=='a' and d2[postman - 1]=='c') or  (d1[postman - 1]=='c' and d2[postman - 1]=='a'):
    print('one')
else:
    print('none')

if d1[milkman - 1]=='a' and d2[milkman - 1]=='a':
    print('both')
elif (d1[milkman - 1]=='a' and d2[milkman - 1]=='c') or  (d1[milkman - 1]=='c' and d2[milkman - 1]=='a'):
    print('one')
else:
    print('none')

if d1[garbageman - 1]=='a' and d2[garbageman - 1]=='a':
    print('both')
elif (d1[garbageman - 1]=='a' and d2[garbageman - 1]=='c') or  (d1[garbageman - 1]=='c' and d2[garbageman - 1]=='a'):
    print('one')
else:
    print('none')
