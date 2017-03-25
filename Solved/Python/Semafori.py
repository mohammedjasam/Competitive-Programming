n, l = map(int, input().split(' '))
pos = 0
res = 0
for i in range(n):
    d, r, g = map(int, input().split(' '))
    res += d-pos
    pos = d
    # print("\ndistance of poll from start")
    # print(d)
    # print("\nETA")
    # print(res)
    # print('distance covered')
    # print(pos)
    aux = res % (r+g)
    print(aux)
    if aux < r:
        res+= r-aux

print (res+(l-pos))








# noOfLights, dest = map(int,input().split())
#
# # print(noOfLights,dest)
# eta=0
# td=dest
# dcov=0
# for i in range(noOfLights):
#
#     d,r,g = map(int,input().split())
#     td-=d
#     dcov+=d
#     print("\ndistance remaining")
#     print(td)
#     print("dis covered")
#     print(dcov)
#     # print(d+r)
#     eta+=d
#     eta+=r
#     print("\nETA")
#     print(eta)
# eta+=td
# td=0
# print("\nfinal distance remaining")
# print(td)
# print("\nfinal ETA")
# print(eta)
