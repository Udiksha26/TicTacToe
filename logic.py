# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.



def make_empty_board():
        return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        ]

def is_player_win(board):
    win = None

def winner(board):
    return None



def next_player(player):
    return  'O'

def checking_winner(board, win_char):
    
    if board[0][0] == board[0][1] == board[0][2] == win_char:   #Checking rows
        return win_char
    elif board[1][0] == board[1][1] == board[1][2] == win_char:
        return win_char
    elif board[2][0] == board[2][1] == board[2][2] == win_char:
        return win_char
    elif board[0][0] == board[1][0] == board[2][0] == win_char:   #checking columns
        return win_char
    elif board[0][0] == board[1][1] == board[2][1] == win_char:
        return win_char
    elif board[0][2] == board[1][2] == board[2][2] == win_char:
        return win_char
    elif board[1][1] == board[2][2] == board[0][0] == win_char:     #checking diagonals
        return win_char
    elif board[0][2] == board[1][1] == board[2][0] == win_char:
        return win_char
    else:
        return None