c=0
code="welcome to code jam"
def run(s,l,index,c):
    # print(c)
    if l==len(code):
        c+=1
        return c
    i=index
    for i in range(len(s)):
        if code[l]==s[i]:
            run(s,l+1,index+1,c)


N= int(input())
for i in range(N):

    s=input()
    print(run(s,0,0,c))

    counter="0000"+str(c)

    counter=counter[:-4]
    print("Case #"+str(i)+": "+counter)
