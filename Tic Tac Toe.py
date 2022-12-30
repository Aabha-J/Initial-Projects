board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9'
         ]


def print_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def check_game():
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X'
    ) or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X'
    ) or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X'
    ) or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X'
    ) or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X'
    ) or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X'
    ) or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X'
    ) or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'
    ):
        print("X Wins")
        return True

    if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O'
    ) or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'
    ) or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O'
    ) or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O'
    ) or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'
    ) or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'
    ) or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'
    ) or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'
    ):
        print("O Wins")
        return True

    elif spots_available == 0:
        print("It's a tie")
        return True

    else:
        return False


def choose_spot():
    spot_valid = False
    while not spot_valid:
        if player1_turn:
            spot = str(input('Choose a spot for X: '))
        if player2_turn:
            spot = str(input('Choose a spot for O: '))
        if spot in board:
            spot_valid = True
            return spot
        if not spot_valid:
            print("Oops you can't go there")


player1_turn = True
player2_turn = False
game_over = False
spots_available = 9

print_board(board)

while not game_over:
    if player1_turn:
        location = int(choose_spot()) - 1
        board[location] = 'X'
        print_board(board)
        spots_available -= 1
        game_over = check_game()
        player2_turn = True
        player1_turn = False

    elif player2_turn:
        location = int(choose_spot()) - 1
        board[location] = 'O'
        print_board(board)
        spots_available -= 1
        game_over = check_game()
        player1_turn = True
        player2_turn = False
