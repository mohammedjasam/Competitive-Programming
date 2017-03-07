cups = [1,2,3]
swaps = input()
swaps = list(swaps)

for i in range(len(swaps)):
    if swaps[i] == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    if swaps[i] == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    if swaps[i] == 'C':
        cups[0], cups[2] = cups[2], cups[0]

print(cups.index(1)+1)
