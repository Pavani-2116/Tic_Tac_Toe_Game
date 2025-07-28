# ai.py
from utils import check_winner, is_draw

def best_move(board, player):
    best_score = -float('inf')
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = player
            score = minimax(board, 0, False, player)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def minimax(board, depth, is_maximizing, player):
    opponent = "O" if player == "X" else "X"
    winner = check_winner(board)

    if winner == player:
        return 1
    elif winner == opponent:
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = player
                score = minimax(board, depth + 1, False, player)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = opponent
                score = minimax(board, depth + 1, True, player)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score
