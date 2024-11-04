def evaluate(board):
    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"

board1 = "---xxx---"
board2 = "---ooo---"
board3 = "oxxxoxoxo"
board4 = "---xox---"

print(evaluate(board1))
print(evaluate(board2))
print(evaluate(board3))
print(evaluate(board4))