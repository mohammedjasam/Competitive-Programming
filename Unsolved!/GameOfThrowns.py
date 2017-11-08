n, k = map(int, input().split())
actions = input()

actions = actions.replace("undo ", "*")
actions = actions.split()
# print(actions)

childQueue = []
for x in range(n):
    childQueue.append(x)

revchildQueue = list(reversed(childQueue))
# print(childQueue, revchildQueue)
current = [0]
# print('a, index location, value at index, current array')
for a in actions:
    try:
        if int(a) > 0:
            current.append(childQueue[(current[-1] + int(a)) % n])
            # print(a, (current[-1] + int(a)) % n, childQueue[(current[-1] + int(a)) % n], current)
            # print(current)
        elif int(a) < 0:
            current.append(revchildQueue[(current[-1] + int(a)) % n])
            # print(a, (current[-1] + int(a)) % n, revchildQueue[(current[-1] + int(a)) % n], current)
            # print(current)

    except:
        if a[0] == "*":
            if int(a[1]) == 0:
                pass
                # print(current)
            else:
                current = current[:-int(a[1])]
            # print(a[1], current)
            # print(Undo)

# print("\n\nFinal Solution")
print(current[-1])
