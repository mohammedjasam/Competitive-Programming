ip = input()
U,L,S,W=0,0,0,0

for i in range(len(ip)):
    if 33<=ord(ip[i])<=126:
        if ord(ip[i])==95:
            W+=1
        if 65<=ord(ip[i])<=90:
            U+=1
        elif 97<=ord(ip[i])<=122 and ord(ip[i])!=95:
            L+=1
        elif 33<=ord(ip[i])<=64 or 91<=ord(ip[i])<=94 or ord(ip[i])==96 or 123<=ord(ip[i])<=126:
            S+=1
print(str(W/len(ip)))
print(str(L/len(ip)))
print(str(U/len(ip)))
print(str(S/len(ip)))
