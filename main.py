from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    global count        #count variable to keep track of moves
    if count == 0:
        count += 1
    print("Enter your move:", end="")
    move = int(input())

    if move <= 3:
        if (board[0][move - 1] != 'X') & (board[0][move - 1] != 'O'): #if in the first column
            board[0][move - 1] = 'O'
            count += 1
        else:
            print("Please choose a valid move")
    elif move <= 6:
        if (board[1][move - 4] != 'X') & (board[1][move - 4] != 'O'): #if in the second column
            board[1][move - 4] = 'O'
            count += 1
        else:
            print("Please choose a valid move")
    elif move > 6 & move <= 9:
        if (board[2][move - 7] != 'X') & (board[2][move - 7] != 'O'): #if in the third column
            board[2][move - 7] = 'O'
            count += 1
        else:
            print("Please choose a valid move")
    else:
        print("Please choose a valid move")
        enter_move(board)
    display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list = []
    for i in range(len(board)):
        for k in range(len(board[i])):
            if (board[i][k] != 'O') & (board[i][k] != 'X'):
                list.append((int(i), int(k)))


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    global winner
    if count >= 5:
        if board[0][0] == board[0][1] == board[0][2] == sign:  # across the top
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[1][0] == board[1][1] == board[1][2] == sign:  # across the middle
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[2][0] == board[2][1] == board[2][2] == sign:  # across the bottom
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][0] == board[1][0] == board[2][0] == sign:  # down left
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][1] == board[1][1] == board[2][1] == sign:  # down middle
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][2] == board[1][2] == board[2][2] == sign:  # down right
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][0] == board[1][1] == board[2][2] == sign:  # top left bottom right diagonal
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][0] == board[1][0] == board[2][0] == sign:  # top right bottom left diagonal
            winner = 1
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")

            # If all spots are filled and nobody won, it's a tie
    if count == 9:
        winner = 1
        print("It's a Tie!!")


def draw_move(board):
    # The function draws the computer's move and updates the board.
    global count
    make_list_of_free_fields(board)
    if count < 9:
        draw = int(randrange(1, 10))
        if draw == 5:
            draw_move(board)
        elif draw <= 3:
            if (board[0][draw - 1] != 'X') & (board[0][draw - 1] != 'O'):
                board[0][draw - 1] = 'X'
                count += 1
            else:
                draw_move(board)
        elif draw <= 6:
            if (board[1][draw - 4] != 'X') & (board[1][draw - 4] != 'O'):
                board[1][draw - 4] = 'X'
                count += 1
            else:
                draw_move(board)
        else:
            if (board[2][draw - 7] != 'X') & (board[2][draw - 7] != 'O'):
                board[2][draw - 7] = 'X'
                count += 1
            else:
                draw_move(board)
        display_board(board)


if __name__ == "__main__":
    count = 1
    winner = 0
    gameboard = ['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']
    display_board(gameboard)
    while (count < 9) | (winner == 0):
        if count % 2 != 0:
            enter_move(gameboard)
        else:
            if winner != 1:
                draw_move(gameboard)
            else:
                break
        if count >= 5:
            victory_for(gameboard, 'X')
            if winner == 1:
                break
            else:
                victory_for(gameboard, 'O')
                if winner == 1:
                    break
