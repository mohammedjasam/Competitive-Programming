"""Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring."""
#
class LongestSubstring:
    maxi = ""
    def find(self, s):
        sub = ""
        lsub = []
        for i in s:
            if not(i in sub):
                # print(i)
                sub += i

            else:
                # print(i)
                lsub.append((len(sub),sub))
                sub = ""
                sub += i

        # sorted(lsub,reverse = True)
        return max(lsub)[1]






s = 'pojasam'
# if 'a' in s:
a = LongestSubstring();
print(a.find(s))
