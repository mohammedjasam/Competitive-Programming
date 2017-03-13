from sys import stdin

input = stdin.readline()

output = ""

i = 0
while i < len(input):
    c = input[i]
    if c in "aeiou":
        output+=c
        i+=2
    else:
        output+=c
    i+=1

print (output)
