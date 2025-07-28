# utils.py

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    return None

def is_draw(board):
    return "" not in board and check_winner(board) is None

def reset_board():
    return [""] * 9
