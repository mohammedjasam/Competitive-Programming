import math



testcases = int(input())
for t in range(testcases):
    candidates = int(input())
    cdV = []
    for c in range(candidates):
        cdV.append(int(input()))

    maxCV = max(cdV)
    minCV = min(cdV)
    midV = sum(cdV)/2

    if not(maxCV == minCV) and maxCV > midV:
        print("majority winner " + str(cdV.index(maxCV) + 1))
        # print(maxCV, midV)
    elif not(maxCV == minCV) and maxCV <= midV:
        print("minority winner " + str(cdV.index(maxCV) + 1))
        # print(maxCV, midV)
    elif maxCV == minCV:
        print("no winner")
