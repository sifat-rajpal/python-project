# Create a board
# display board
# play game
# handle turn
# check for win
# check row
# check columns
# check diagonal
# check for tie


# ------- Global variable --------
game_still_going = True
# The player if x goes first
player = "X"
# Who won
winner = None


# Printing the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Staring the game
def play_game():
    display_board()

    while game_still_going:
        handle_turn()
        check_for_winner()
        flip_player()
    # print(game_still_going)
    if winner == "X" or winner == "O":
        print(winner + "won.")
    else:
        print("tie")


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def handle_turn():
    print(player + "'s turn")
    position = input("Choose where you want to play to : ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose from 1 - 9 : ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't input there try again")

        board[position] = player
        display_board()


def check_for_winner():

    global winner

    row_winner = check_row()
    # check_columns
    columns_winner = check_columns()
    # check_diagonals
    diagonals_winner = check_diagonals()
    # check_tie
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None


def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"
    if columns_1 or columns_2 or columns_3:
        game_still_going = False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    else:
        return None
    return


def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    else:
        return None
    return


def flip_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return


play_game()
