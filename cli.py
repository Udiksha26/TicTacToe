# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import checking_winner

players = {
    True : "Player 1 (0)",
    False : "Player 2 (X)"
}


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    Move = True
    move_number = 0
    while (move_number < 9 and winner == None):
        print("Take your chance !")
        print(board)
        row = int(input("Enter the row number (0-2) : ")) # Getting desiredinput location from user
        column = int(input("Enter the column number (0-2) : "))
        if Move:
            board[row][column] = 'O' #Placing user move input on the board
            winner = checking_winner(board, 'O')
        else:   
            board[row][column] = 'X' 
            winner = checking_winner(board, 'X')
        move_number += 1  #Tracking number of moves left
        Move = not Move # Move Update
    if winner == None:
        print("Draw")
    else:
        print(" is the winner!! ")
    