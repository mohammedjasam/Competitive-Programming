A = input()
if len(A)>50:
    pass
else:
    T,C,G=0,0,0
    # pts=0

    for i in range(len(A)):
        if A[i]=='T':
            T+=1
        elif A[i]=='C':
            C+=1
        elif A[i]=='G':
            G+=1
    # print(T,C,G)
    if T <= C | T <= G:
        smallest = T
    elif C <= G:
        smallest = C
    else:
        smallest = G

    T = T*T
    C = C*C
    G = G*G

    # print(smallest)
    pts = T+C+G+(7*smallest)
    print(pts)
