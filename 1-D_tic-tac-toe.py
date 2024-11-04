def evaluate(board):
    """This function evaluates the game board. 
    If x wins, returns 'x'
    if O wins, returns 'o'
    if it's draw, returns '!'
    if the game is not finished, returns '-' """

    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"

def move(board, mark, position):
    """This function is one move in tic-tac-toe, 
    it takes the current game board, 
    the mark (x or o) and 
    the position (0-19), where the mark should be added.
    And returns an updated game board."""

    if board[position] == "-":
        if position == 0:
            new_board = mark + board[1:]
        elif position == 19:
            new_board = board[:19] + mark
        elif position > 0 and position < 19:
            new_board = board[:position] + mark + board[position +1 :]
        return new_board
    else:
        print("position occupied")
        return board
        

board1 = "--------------------"
board2 = "oxox---------------o"

print(move(board2, "x", 10))

print(evaluate(board2))