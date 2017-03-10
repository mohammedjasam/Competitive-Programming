N = int(input())

for x in range(N):
    Letters = []
    for x in range(97,123,1):
        Letters.append(chr(x))
    s = input()
    s = s.lower()

    for letter in s:
        if letter in Letters:
            Letters.remove(letter)
    if len(Letters) == 0:
        print('pangram')
    else:
        print('missing',end=' ')
        for letter in Letters:
            print(letter,end="")
        print()
