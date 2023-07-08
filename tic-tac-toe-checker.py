def is_solved(board):
    for number in (1,2):
        if linechecker(number, board):
            return number
        elif rowchecker(number, board):
            return number
        elif vertivalchecker(number, board):
            print("vert")
            return number
    if isnotfinished(board):
        return -1
    return 0


def linechecker(num, board):
    for line in board:
        if line.count(num) == 3:
            return True
    return False

def rowchecker(num, board):
    for i in (0,1,2):
        if board[0][i] == num and board[1][i] == num and board[2][i] == num:
            return True
    return False

def vertivalchecker(num, board):
    if board[0][0] == num and board[1][1] == num and board[2][2] == num:
        return True
    elif board[0][2] == num and board[1][1] == num and board[2][0] == num:
        return True
    return False

def isnotfinished(board):
    count = 0
    for line in board:
        count += line.count(0)
    if count > 2:
        return True
    return False

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]

print(is_solved(board))


"""
, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
"""