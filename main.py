from random import randrange
count = 0
board = ['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']


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
    if count==0:
        count+=1
    print("Enter your move:")
    move=int(input())

    if move<=3:
        if (board[0][move-1] != 'X') & (board[0][move-1] != 'O'):
            board[0][move - 1] = 'O'
            count += 1
    elif move>3 & move<=6:
        if board[1][move-4] != 'X' & board[1][move-4] != 'O':
            board[1][move-4] = 'O'
            count += 1
    elif move>6 & move<=9:
        if board[2][move-7] != 'X' & board[2][move-7] != 'O':
            board[2][move-7] = 'O'
            count += 1
    else:
        print("Please choose a valid move")
        enter_move(board)

def make_list_of_free_fields(board):
# The function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers.
    list=[]
    for i in range(len(board)):
        for k in range(len(board[i])):
            if (board[i][k] != 'O') & (board[i][k] != 'X'):
                list.append((i,k))


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if count >= 5:
        if board[0][0] == board[0][1] == board[0][2] == sign:  # across the top
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[1][0] == board[1][1] == board[1][2] == sign:  # across the middle
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[2][0] == board[2][1] == board[2][2] == sign:  # across the bottom
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][0] == board[1][0] == board[2][0] == sign:  # down left
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][1] == board[1][1] == board[2][1] == sign:  # down middle
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][2] == board[1][2] == board[2][2] == sign:  # down right
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][0] == board[1][1] == board[2][2] == sign:  # top left bottom right diagonal
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")
        elif board[0][0] == board[1][0] == board[2][0] == sign:  # top right bototm left diagonal
            display_board(board)
            if sign == 'O':
                print("You won!")
            else:
                print("The Computer Won!")

            # If all spots are filled and nobody won, it's a tie
    if count == 9:
        print("It's a Tie!!")

def draw_move(board):
    # The function draws the computer's move and updates the board.
    make_list_of_free_fields(board)
    draw = randrange(1,9)
    if draw == 5:
        draw_move(board)
    elif draw<=3:
        if (0, draw-1) in list:
            board[0][draw-1] = 'X'
        else:
            draw_move(board)
    elif draw>3 & draw<=6:
        if (1, draw - 4) in list:
            board[1][draw - 4] = 'X'
        else:
            draw_move(board)
    else:
        if (2, draw - 7) in list:
            board[2][draw - 7] = 'X'
        else:
            draw_move(board)