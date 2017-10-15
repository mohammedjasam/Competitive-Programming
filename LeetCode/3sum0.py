s = [-1, 0, 1, 2, -1, -4]
l = []


### O(N^3) complexity
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         for k in range(j+1,len(s)):
#             if s[i] + s[j] + s[k] == 0:
#                 if sorted([s[i],s[j],s[k]]) not in l:
#                     l.append([s[i],s[j],s[k]])
# print(l)


### O(N) complexity
l = []
for i in range(len(s)):
    if i < len(s)-1:
        a = s[i]
        b = s[i+1]
        if -(a+b) in (s[i+1:]):
            if sorted([a,b,-(a+b)]) not in l:
                l.append([a,b,-(a+b)])
print(l)
