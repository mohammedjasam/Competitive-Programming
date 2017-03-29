s = input()
d = {i:s.count(str(i)) for i in range(10)}
print(d)
digs = sorted(sorted(d.keys()), key=lambda x: d[x])
print(digs)
done = False
for i in range(1, 10):
    if d[i] == 0:
        print(i)
        done = True
        break

if not done:
    least_common_num = digs[0]
    if least_common_num == 0:
        #edge case
        if d[0]  < d[digs[1]]:
            print('1' + '\0'*(d[0]+1))
            done = True
        else:
            least_common_num = digs[1]
    if not done:
        print(str(least_common_num)*(d[least_common_num]+1))

# import itertools
# s=input()
# s=list(s)
# s=[int(x) for x in s]
# # print(s)
# least=1
# st=[]
# for x in s:
#     st.append(x)
# # print(st)
# for i in range(len(s)):
#     for j in range(len(s)):
#         if i!=j:
#             # print()
#             st.append(int(str(s[i])+str(s[j])))
# st.sort()
# # print(st)
# st=list(set(st))
# print(st)
# for i in range(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
#     if i in st:
#         pass
#     else:
#         least=i
#         break
# print(least)
