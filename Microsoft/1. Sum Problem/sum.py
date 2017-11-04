with open('data.txt') as f:
        for line in f:
            line = line[:-1]
            s=line.split(',')
            s = [int(x) for x in s]
            r = round(sum(s)/len(s))

            print(r)
            # if
