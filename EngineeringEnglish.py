import sys
for line in sys.stdin:
    wordlist=line.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append((wordlist.count(w),w))
    print("List\n" + str(wordlist) + "\n")
    print("Frequencies\n" + str(wordfreq) + "\n")
