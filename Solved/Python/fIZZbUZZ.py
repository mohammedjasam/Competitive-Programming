s = [int(x) for x in input().split()]

for i in range(1, s[2]+1):
    if i % s[0] == 0:
        if i % s[1] == 0:
            print("FIZZBUZZ")
        else:
            print("FIZZ")
    elif i % s[1] == 0:
        print("BUZZ")
    else:
        print(i)
