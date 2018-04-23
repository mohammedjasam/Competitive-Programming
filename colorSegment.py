t = int(input())


for j in range(t):
    S = int(input())
    line = input().split()

    blue = []
    red = []
    for i in range(len(line)):
        if line[i][-1] == "B":
            blue.append(int(line[i][:-1]))
        else:
            red.append(int(line[i][:-1]))
    blue = list(sorted(blue, reverse = True))
    red = list(sorted(red, reverse = True))

    if S > 1:
        small = 0
        if S - (len(blue) + len(red)) < S:
            if len(blue) > len(red):
                for i in range(len(blue) - len(red)):
                    del blue[-1]
                small = len(red)
            else:
                small = len(blue)
                for i in range(len(red) - len(blue)):
                    del red[-1]
        else:
            small = len(red)
        result = (sum(red[:small]) + sum(blue[:small])) - (small * 2)
    else:
        result = 0
    print("Case #%d:" %(j + 1), result)
