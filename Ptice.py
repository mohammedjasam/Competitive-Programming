Alist = ['A', 'B', 'C']
Blist = ['B', 'A', 'B', 'C']
Clist = ['C', 'C', 'A', 'A', 'B', 'B']

numQuestions = int(input())
answers = input()

def score(lst):
    score = 0
    index = 0  # increment for each compare, reset for len(lst)
    for c in answers:
        if lst[index] == c:
            score += 1
        index += 1
        if index == len(lst):
            index = 0  # reset
    return score


# scores given a list of sequential answers
Ascore = score(Alist)
Bscore = score(Blist)
Cscore = score(Clist)

maxScore = max(Ascore, Bscore, Cscore)
print(maxScore)  # mandatory

if(Ascore == maxScore):
    print("Adrian")
if(Bscore == maxScore):
    print("Bruno")
if(Cscore == maxScore):
    print("Goran")
