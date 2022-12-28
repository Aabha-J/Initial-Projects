import random


def play(highest, chances):
    num = random.randint(1, highest)
    guess = int(input(f"Enter a number between 1 and {highest}. You have {chances} chances: "))
    chance = 1
    while chance <= chances:
        if num == guess:
            print('You win')
            break
        elif chance == chances:
            print(f'You lose the number was {num}.')
            chance += 1
        elif guess < num:
            print("Too low")
            print(f"You have {chances - chance} chances left")
            guess = int(input('Try again: '))
            chance += 1
        elif guess > num:
            print('Too high')
            print(f"You have {chances - chance} chances left")
            guess = int(input('Try again: '))
            chance += 1


play(60, 5)







