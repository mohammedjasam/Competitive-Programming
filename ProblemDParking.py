a1,b1,c1=map(int,input().split())
price=[]
price.append(a1)
price.append(b1)
price.append(c1)
a=[]
d=[]
total=0
x1, y1 = map(int, input().split())
a.append(x1)
d.append(y1)
x2, y2 = map(int, input().split())
a.append(x2)
d.append(y2)
x3, y3 = map(int, input().split())
a.append(x3)
d.append(y3)

for i in range(100):
    cars=0
    for j in range(3):
        cars+= 1 if (i  >= a[j] and i < d[j]) else 0
    total+=cars*price[cars-1]
print(total)



# a1,b1,c1=map(int,input().split())
# t1,t2,t3 = {},{},{}
#
# x1, y1 = map(int, input().split())
# for i in range(101):
#     if x1<= i <=y1:
#         t1[i]=1
#     else:
#         t1[i]=0
#
# x2, y2 = map(int, input().split())
# for i in range(101):
#     if x2<= i <=y2:
#         t2[i]=1
#     else:
#         t2[i]=0
#
# x3, y3 = map(int, input().split())
# for i in range(101):
#     if x3<= i <=y3:
#         t3[i]=1
#     else:
#         t3[i]=0
# minx,maxy=[],[]
# minx.append(x1)
# minx.append(x2)
# minx.append(x3)
#
# maxy.append(y1)
# maxy.append(y2)
# maxy.append(y3)
#
# mx=min(minx)
# my=max(maxy)
# price=0
# for i in range(mx,my+1):
#     if t1[i]==1 and t2[i]==1 and t3[i]==1:
#         price+=3
#     elif (t1[i]==1 and t2[i]==1 and t3[i]==0) or (t2[i]==1 and t3[i]==1 and t1[i]==0) or (t3[i]==1 and t1[i]==1 and t2[i]==0):
#         price+=6
#     elif (t1[i]==1 and t2[i]==0 and t3[i]==0) or (t2[i]==1 and t3[i]==0 and t1[i]==0) or (t3[i]==1 and t1[i]==0 and t2[i]==0):
#         price+=5
#
# print(price)
