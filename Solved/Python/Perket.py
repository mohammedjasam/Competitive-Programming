import itertools
from itertools import *
from functools import reduce


num = input()
ingredients = []

for i in range(int(num)):
	s, b = map(int, input().split(' '))
	ingredients.append((s,b))
# print(ingredients)
min = 1000000000

# print(x for x in itertools.combinations(ingredients,2))
for i in range(len(ingredients)):
	combinations = itertools.combinations(ingredients, i+1)

	for s in combinations:

		total = reduce((lambda t1, t2: (t1[0]*t2[0], t1[1]+t2[1])), s)
		total = abs(total[0]-total[1])
		if total < min:
			min = total
print (min)
