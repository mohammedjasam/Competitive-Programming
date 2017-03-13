N = int(input())

for i in range(N):
    s=input()
    if "simon says" in s.lower():
        print(s[11:])
    else:
        print()
