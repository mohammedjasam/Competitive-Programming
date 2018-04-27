import sys



days = []
nameTime = {}
gate = False
for line in sys.stdin:
    print(nameTime)
    line = line[:-1]
    if line == "OPEN":
        gate = True
    elif gate == True:
        s = line.split()
        print(s)
        if s[0] == "ENTER":
            nameTime[s[1]] = s[2]
        elif s[0] == "EXIT":
            st = nameTime[s[1]]
            nameTime[s[1]] = (int(s[2]) - int(st)) * 0.10
    elif line == "CLOSE":
        gate = False
        days.append(nameTime)
        nameTime = {}

for x in range(len(days)):
    print("Day " + str(x+1))
    for k, v in days[x].items():
        print(k, "$" + v)
    print()
# print(days)
