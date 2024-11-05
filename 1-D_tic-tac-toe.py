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

#def move(board, mark, position):
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
    """This function asks the player for the desired position;
    checks if it is a valid position; 
    and if it is a valid position, it returns the desired position as an integer"""

    while True:
        position = input("Which position do you want to mark? (0-19) ")
        try:
            position = int(position)
            if position >= 0 and position <= 19:
                return position
            else:
                print("Please enter an integer between 0-19.")
        except:
            print("Please enter an integer between 0-19.")
            
def move_is_possible(board):
    if board[position()] == "-":
        return True
    else:
        print("Position occupied.")
        return False

#def player_move(board):
    """This function asks the player for the position,
    returns the new game board or 
    if the position is occupied asks for a new position."""
    player_mark = 'x'
    move(board, player_mark, position())

board1 = "--------------------"
board2 = "oxox---------------o"

print(move_is_possible(board2))

print(evaluate(board2))