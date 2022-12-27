import random

again = True


def play():
    user = input("r for rock, p for paper, s for scissors : ")

    if user == 'p' or user == 'r' or user == 's':
        computer = random.choice(['r', 'p', 's'])
        print(computer)

        if user == computer:
            return "Tie"

        elif (user == 'p' and computer == "r") or (user == 'r' and computer == 's') or \
                (user == 's' and computer == 'p'):
            return 'You win'

        else:
            return 'You lose'
        
    else:
        return 'Invalid Input'


while again == True:
    print(play())
    ask = input("Want to play again, 'y' for yes and 'n' for no: ")
    if ask == 'y' or ask == 'Y':
        again = True
    else:
        again = False
