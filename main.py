from random import randrange

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


display_board(board)
# def enter_move(board):
# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
# The function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
# The function analyzes the board's status in order to check if
# the player using 'O's or 'X's has won the game


# def draw_move(board):
# The function draws the computer's move and updates the board.
