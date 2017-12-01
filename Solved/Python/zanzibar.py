def count_imported_turtles(turtles):
	imported_turtles = 0
	previous = turtles[0]
	for current in turtles[1::]:
		if current == "0":
			print(imported_turtles)
			break
		else:
			if current > (2 * previous):
				imported_turtles += current - 2 * previous
			previous = current
	return imported_turtles


t = int(input())
for _ in range(t):
	l = [int(token) for token in input().split()]
	r = count_imported_turtles(l)
	print(r)
