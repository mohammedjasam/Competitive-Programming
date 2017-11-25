movies = ["jasam", "pooja", "weer", "shalini", "ross"]

import random as rn

def run():
    element = movies[rn.randint(0,4)]
    print(element)
    correct = ""
    for i in element:
        correct += "_"


    for i in range(10):
        guess = input()

        indices = []
        for i in range(len(element)):
            if guess == element[i]:
                indices.append(i)

        for i in indices:
            a = list(correct)
            a[i] = guess[0]
            correct = "".join(a)

        if correct == element:
            print(correct)
            break

        print(correct)

run()
