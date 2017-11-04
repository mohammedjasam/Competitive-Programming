import numpy as np
with open('data.txt') as f:
    combo=[]
    for line in f:
        line = line[:-1]
        s = line.split(" ")
        combo.append(s)
    a = np.array(combo)
    a = a.transpose()
    string = ""
    for x in a:
        for j in x:
            string = string + j
            string = string +  " "
        string = string[:-1]
        string = string + "\n"
    print(string)
