from random import randrange

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
            
def move_is_possible(board, position):
    if board[position] == "-":
        return True
    else:
        print(f"{position}. position occupied.")
        return False

def move(board, mark, position):
    """This function is one move in tic-tac-toe, 
    it takes the current game board, 
    the mark (x or o) and 
    the position (0-19), where the mark should be added.
    And returns an updated game board."""

    if position == 0:
        new_board = mark + board[1:]
    elif position == 19:
        new_board = board[:19] + mark
    elif position > 0 and position < 19:
        new_board = board[:position] + mark + board[position +1 :]
    return new_board
        
def player_move(board):
    """This function asks the player for the position (position function),
    if the position is occupied (move_is_possible function) 
    asks for a new position (position function)
    and if position is not occupied returns the new board (move function)."""
    player_mark = 'x'
    player_position = position()
    while move_is_possible(board, player_position) == False:
       player_position = position()
    return move(board, player_mark, player_position)

def pc_move(board):
    """This function randomly selects a position
    if the position is occupied (move_is_possible function) 
    randomly selects a new position (position function)
    and if position is not occupied returns the new board (move function)."""
    player_mark = 'o'
    player_position = randrange(0, 20)
    while move_is_possible(board, player_position) == False:
       player_position = randrange(0, 20)
    return move(board, player_mark, player_position)

def pc_strategy_move(board):
    player_mark = 'o'
    if "-xx-" in board:
        player_position = board.index('-xx-')
    elif "oxx-" in board:
        player_position = board.index('oxx-') + 3
    elif "-xxo" in board:
        player_position = board.index('-xxo')
    elif "-xx" in board:
        player_position = board.index('-xx')
    elif "xx-" in board:
        player_position = board.index('xx-') + 2
    elif "-x-" in board:
        player_position = board.index('-x-')
    elif "ox-" in board:
        player_position = board.index('ox-') + 2
    elif "-xo" in board:
        player_position = board.index('-xo')  
    elif "-x" in board:
        player_position = board.index('-x')
    elif "x-" in board:
        player_position = board.index('x-') + 1
    else:
        player_position = randrange(0, 20)
        while move_is_possible(board, player_position) == False:
            player_position = randrange(0, 20)
    return move(board, player_mark, player_position)

def tictactoe_1d():
    """This function is the whole tic-tac-toe. 
    The player and the pc moves alternately until someone wins.
    The board is evaluated after each round (evaluate function)."""
    board = "--------------------"
    while evaluate(board) == "-":
        board = player_move(board)
        print(board)
        board = pc_strategy_move(board)
        print(board)
    # End of game
    if evaluate(board) == "x":
        print("Congratulations, you won!")
    elif evaluate(board) == "o":
        print("Unfortunately you didn't win this time.")
    elif evaluate(board) == "!":
        print("It's a tie.")