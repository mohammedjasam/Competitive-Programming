N = int(input())
for i in range(N):
    input() #skip empty line
    amounts = [int(x) for x in input().split()]
    G = input().split()
    M = input().split()
    if max(G)>=max(M):
        print("Godzilla")
    elif max(G)<max(M):
        print("MechaGodzilla")
    else:
        pass
