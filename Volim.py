player = int(input())  # starts with box
rounds = int(input())  # amount of questions
time_left = 210  # seconds left

for x in range(rounds):
    time, response = input().split()
    time_left = time_left - int(time)
    if time_left <= 0:
        break
    if response == 'P' or response == 'N':
        continue
    else:
        if player == 8: # last player on the round table. going in cicrcle.
            player = 1
        else:
            player += 1


print(player)
