import os
import platform


def get_new_board(dimension):
    """
    Return a multidimensional list that represents an empty board (i.e. empty string at every position).
    :param: dimension: integer representing the nxn dimension of your board.
            For example, if dimension is 3, you should return a 3x3 board
    :return: For example if dimension is 3x3, you should return:
                --> [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]
    """
    empty_map = []
    if dimension <= 0:
        return empty_map

    for _ in range(dimension):
        empty_map.append([" " for _ in range(dimension)])
    return empty_map


def add_x_at_position(board, position):
    """
    Edit the given board by adding "X" to the given position. *Don't* return anything! Just edit the board argument.
    For example if board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] and position == (1,2), the board should become:
    --> [[" ", " ", " "],
         [" ", " ", "X"],
         [" ", " ", " "]]
    :param board: multidimensional list representing the current state of the game board
    :param position: a tuple with as first element the row number and as second element the column number.
           For example: (2,3) --> the position at the 3rd row and 4th column
    """
    if position[0] in [*range(0, len(board)+1)] and position[0] in [*range(0, len(board)+1)]:
        board[position[0]][position[1]] = "X"


def add_o_at_position(board, position):
    """
    Exactly the same as "add_x_at_position()" but instead of adding "X" you add "O" (big o, not zero 0).
    """
    if position[0] in [*range(0, len(board)+1)] and position[0] in [*range(0, len(board)+1)]:
        board[position[0]][position[1]] = "O"


def get_board_representation(board):
    """
    Return a string representing the entire board as how you are supposed to print it.
    Outside the function you should be able to do the following in order to print the string:
    print(get_board_representation(board)).

    For more details about how exactly the representation should look like, take a look at the test file.
    :param board: A multidimensional list representing the board
    :return a string representation of the current state of the given board (see tests for details)
    """
    '\n'.join(map(str, board))


def player_x(board):
    """
    Let player X play his turn. You should first ask him for input. Ask him for the row and the column where he wants
    to put the next X. You should be cautious with every case:
    * If the given position is empty, you should place the X (don't return anything, just edit the given board).
    * If the position is outside the boundaries of the given board, you shouldn't edit the board and should print a
      message to inform the user that his input is invalid and give him another chance.
    * If the given position is already occupied, you should also not edit the board and should print a message to inform
      the user that the position is already occupied and give him another chance.

    There are no tests for this function. So make sure you find a way to test it yourself.

    :param board: A multidimensional list representing the board
    """
    pass  # TODO




def player_o(board):
    """
    Let player O play his turn. Just like player_x. And if you are smart, you will make an extra helper
    function to avoid code duplication.

    There are no tests for this function. So make sure you find a way to test it yourself.
    """
    pass  # TODO


def is_game_finished(board):
    """
    Return true if the game is finished and false if it isn't.
    A game is finished when one of two players won, or when all the cells of the board were filled.
    :param board: A multidimensional list representing the board
    :return: True or False, signaling whether the game is finished.
    """
    pass  # TODO


def get_winner(board):
    """
    Return the winner of this game based on given board.
    If the winner is player X, you should return "player X".
    If the winner is player Y, you should return "player Y".
    If this game is not yet finished or if there is no winner, you should return None (not a string, it's valid Python).

    :param board: A multidimensional list representing the board
    :return: "player X" or "player Y" or None
    """
    pass  # TODO


if __name__ == '__main__':
    # Everything below is already implemented for you. Don't edit it ! It represents the logic of the game using your
    # functions. This should only work correctly if your functions work correctly.

    print("############################")
    print("# Welcome to TIC TAC TOE ! #")
    print("############################")

    # Ask for the board dimension
    dimension = input("Choose a dimension for your board: ")
    while not dimension.isdigit():
        print("You did not give a (positive) integer, Try again !")
        dimension = input("Choose a dimension for your board: ")

    # Generate this new board and print its representation
    board = get_new_board(int(dimension))
    print(get_board_representation(board))

    # Ask for user input by alternating between both players (X and O)
    alternate = 0
    while not is_game_finished(board):
        if alternate == 0:
            player_o(board)
            alternate = 1
        elif alternate == 1:
            player_x(board)
            alternate = 0

        # Clear everything and print the new board representation
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')  # TODO: if you have problems remove this line and the else before it
        print(get_board_representation(board))

    # Print who's the winner (if any)
    winner = get_winner(board)
    if winner is None:
        print("DRAW!\nThis game is finished and there is no winner.")
    else:
        print(f"FINISHED!\nThe winner of this game is: {winner} !")
