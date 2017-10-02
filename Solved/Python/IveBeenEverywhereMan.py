def is_simple_name(city_name):
	if len(city_name) > 0:
		for character in city_name:
			character = str(character)
			if character.islower() and not character.isspace() and character.isalpha():
				continue
			else:
				return False
		return True
	else:
		return False


t = int(input())
for _ in range(t):
	n = int(input())
	count = 0
	cities_set = set()
	for i in range(n):
		city = input()
		if city not in cities_set:
			cities_set.add(city)
			if is_simple_name(city):
			
