import re
a = input()
l = []
for x in a:
    if x == " ":
        pass
    else:
        # print(x)
    # print(ord(x))

    if (64<ord(x)<90) or (97<ord(x)<122):
        l.append(x)

print(l)
length = len(l)
newL = []
file = open('words.txt', 'r')

for line in file.readlines():
    count = 0
    for x in l:
        if x in line:
            count+=1
            pass
        else:


# #     count = 0
# #     for x in l:
# #         # print(x)
# #         if x in l:
# #             continue
# #         else:
# #             pass
# ll=[]
# for x in l:
#     for line in file.readlines():
#         if x in line:
#             ll.append((x,line))






        # if x in line:
        #     print(x,line)
        #     count+=1
        #     continue
        # else:
        #     break
        # if count == length:
        #     print(line)

#             print(count)
#             count += 1
#     if count == length:
#         newL.append(line)
# print(newL)


        # print(line)
        # i+=1
