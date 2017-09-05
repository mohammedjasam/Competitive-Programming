import sys

s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
# print(s) Converted the string to list
d1 = {}
d2 = {}
for i in range(len(s)):
    d1[i]=s[i]
    d2[s[i]]=i
# print(d1)
# print(d2)
# print(d1)# Created a dict with chars as keys and numbers as values
for ip in range(30):
    inp = input()
    if len(inp) == 1:
        sys.exit()
    move, string = inp.split()

    # print(move,string)
    move = int(move)
    string = list(string)
    # print(string)
    ans = []
    fin = []
    for i in string:
        ans.append(d2[i])
    # print(ans)

    for i in ans:
        if (i+move)<28:
            fin.append(d1[i+move])
        else:
            fin.append(d1[(i+move)%28])
    fin=list(reversed(fin))

    res = ""
    for i in fin:
        res+=i
    print(res)
