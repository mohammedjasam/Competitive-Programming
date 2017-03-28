n = int(input())

for i in range(n):
    s=input().split()
    # s=list(s)
    k=s[0]
    del s[0]
    # print(k)
    # print(s)

    subseq=[]
    for x in range(len(s)):
        try:
            if s[x]<s[x+1]>s[x+2]:
                print(s[x+1])
            elif s[x]<s[x+1]<s[x+2]:
                print(s[x+2])
                if s[x]<s[x+2]>s[x+3]:

        except:
            pass
    print(subseq)
