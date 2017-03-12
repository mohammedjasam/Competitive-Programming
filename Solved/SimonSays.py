N=int(input())

for i in range(N):
    Words = input()
    if Words.startswith("Simon says"):
        print(" ".join(Words.split()[2:]))
