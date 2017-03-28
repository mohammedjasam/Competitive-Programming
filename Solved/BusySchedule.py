import sys
for n in sys.stdin:
    if n[:-1]=='0':
        break
    else:
        H,M,Z,T=[],[],[],[]
        for i in range(int(n)):

            s=input()
            newstr=""
            for x in range(len(s)):
                if s[x]==" ":
                    newstr+=":"
                else:
                    newstr+=s[x]
            h,m,z=newstr.split(":")
            H.append(int(h))
            M.append(int(m))
            Z.append(z)
        for x in range(len(H)):
            if Z[x]=='a.m.':
                if H[x]==12:
                    T.append((M[x],x+1))
                else:
                    T.append((((H[x]*60)+(M[x])),x+1))
            elif Z[x]=='p.m.':
                if H[x]==12:
                    T.append(((M[x]+720),x+1))
                else:
                    T.append((((H[x]*60)+(M[x])+720),x+1))
        T.sort()
        srtList=[]
        for x in (T):
            srtList.append(x[1])
        for x in srtList:
            i=x-1
            a=str(M[i])
            if len(a)==1:
                a="0"+str(M[i])
                print(str(H[i])+":"+a+" "+ Z[i] )
            else:
                print(str(H[i])+":"+str(M[i])+" "+ Z[i] )
        print()
