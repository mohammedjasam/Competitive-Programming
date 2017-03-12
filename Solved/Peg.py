count = 0

h1 = input()
h2 = input()
h3 = input()
h4 = input()
h5 = input()
h6 = input()
h7 = input()

grid = [list(h1), list(h2), list(h3), list(h4), list(h5), list(h6), list(h7)]

#checks columns for substrings.
def checkvertical(substring1, substring2):
    count = 0
    for j in range(5):
        for i in range(7):
            if grid[j][i] + grid[j+1][i] + grid[j+2][i] == substring1 or grid[j][i] + grid[j+1][i] + grid[j+2][i] == substring2:
                count += 1

    return count


# counts amount of two given substrings in a string
def checkhorizontal(strings, substring1, substring2):
    count = 0
    for x in range(5):
        if strings[x:x + 3] == substring1 or strings[x:x + 3] == substring2:
            count += 1
    return count


for x in range(7):
    count += checkhorizontal(h1, 'oo.', '.oo')

count += checkvertical('oo.', '.oo')

print(count)
