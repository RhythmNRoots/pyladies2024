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
        
def position():
    """This function asks the player for the position desired
    checks if it is a valid position and if it is a valid position 
    it returns the desired position"""    
    while True:
        new_position = input("Which position do you want to mark? (0-19) ")
        try:
            new_position = int(new_position)
            if new_position >= 0 and new_position <= 19:
                return new_position
            else:
                print("Please enter an integer between 0-19.")
        except:
            print("Please enter an integer between 0-19.")

def player_move(board):
    """This function asks the player for the position,
    returns the new game board or 
    if the position is occupied asks for a new position."""
    player_mark = 'x'
    return move(board, player_mark, position())

board1 = "--------------------"
board2 = "oxox---------------o"

print(player_move(board2))

print(evaluate(board2))