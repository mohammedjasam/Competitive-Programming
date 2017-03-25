testcases = int(input())
oddman = 0
for x in range(testcases):
    guestNumber = int(input())
    guests = map(int,input().split())
    guests = list(guests)
    for num in guests:
        if guests.count(num) == 1:
            print('Case #' + str(x+1) + ': ' + str(num))
