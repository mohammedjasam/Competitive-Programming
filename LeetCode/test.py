def longestPlaString(s):
    maxLen = 1
    start = 0
    length = len(s)
    low = 0
    high = 0

    for i in range(1, length):
        low = i-1
        high = i
        while low>=0 and high <length and s[low] == s[high]:
            if (high - low + 1)>maxLen:
                start = low
                maxLen = high - low + 1
            low -= 1
            high += 1

        low = i-1
        high = i+1
        while low>=0 and high <length and s[low] == s[high]:
            if (high - low + 1)>maxLen:
                start = low
                maxLen = high - low + 1
            low -= 1
            high += 1

    print(len(s[start:start+maxLen]),s[start:start+maxLen])
longestPlaString("bacbaabcabbaccccaaaaaaaaaaaaaaaaaaaaaaaacccccab")
