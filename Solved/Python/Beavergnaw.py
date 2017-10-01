import math

while True:
	d, v = map(int, input().split())
	if (d == 0) and (v == 0):
		break
	else:
		r = ((math.pi*d**3 - 6*v) / math.pi)**(1/3)
		print(r)
