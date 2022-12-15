# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


import random

class TicTacToe:

    
    game_type = {1: "Another Person", 2: "Bot"}
    human_players = {True: "Player 1 (0)", False: "Player 2 (X)"}

    def __init__(self) -> None:
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    def is_another_person(self):
        print("Game between")
        print("1. Human ")
        print("2. Computer ")
        self.gtype = int(input(" Choice : "))
        return True if self.gtype == 1 else False

    def print_board(self):
        for row in self.board:
            print(*row)

    def check_win(self, winning):
        board = self.board
        if board[0][0] == board[0][1] == board[0][2] == winning: #Checking rows
            return winning
        elif board[1][0] == board[1][1] == board[1][2] == winning:
            return winning
        elif board[2][0] == board[2][1] == board[2][2] == winning:
            return winning
        elif board[0][0] == board[1][0] == board[2][0] == winning: #checking columns
            return winning
        elif board[0][1] == board[1][1] == board[2][1] == winning:
            return winning
        elif board[0][2] == board[1][2] == board[2][2] == winning:
            return winning
        elif board[1][1] == board[2][2] == board[0][0] == winning:  #checking diagonals
            return winning
        elif board[0][2] == board[1][1] == board[2][0] == winning:
            return winning
        else:
            return None

    def bot_move(self):
        board = self.board
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] != None:
            self.bot_move()
        else:
            board[row][column] = "O"
            return board

    def play_with_human(self):
        winner = None
        chance = True
        move_number = 0
        while move_number < 9 and winner == None:
            print(f"Take a turn {self.human_players[chance]}!")

            
            self.print_board()         # User can see the board

           
            row = int(input("Enter the row number (0-2) : "))          # Asking move from user
            column = int(input("Enter the column number (0-2) : "))

           
            if self.board[row][column] != None:              # Asking users not to use the same spot
                print("Please play the move in another empty spot!")
                continue

            if chance:
                self.board[row][column] = "X"
                winner = self.check_win("X")
            else:
                self.board[row][column] = "O"
                winner = self.check_win("O")

          
            move_number += 1                      # Increment the number of moves played
           
            chance = not chance

        if winner == None:
            print("Game is draw")
        else:
            print(f"{self.human_players[not chance]} is the winner!! ")
        return winner

    def playing_with_bot(self):
        winner = None
        chance = True
        move_number = 0
        print("checkpoint")
        while move_number < 9 and winner == None:

            print("Please take a turn")

            
            self.print_board()                           # Show the board to the user

            
            row = int(input("Enter the row number (0-2) : "))        # Input a move from the player
            column = int(input("Enter the column number (0-2) : "))

           
            if self.board[row][column] != None:                   # Do not allow players to play the same square
                print("Please play the move in an empty square!")
                continue

            self.board[row][column] = "X"
            if self.check_win("X"):
                print("****Congratulations You Win!****")
                winner = "X"
                return "X"
            

            self.bot_move()

            if self.check_win("0"):
                print("You lost! Better luck next time. :( ")
                winner = "0"
                return "0"

            
            move_number += 2
           
            if winner == None:
               pass
            else:
                print(f"{self.human_players[not chance]} is the winner!! ")
                return winner
        if winner == None:
            print ("Draw")
            winner = "draw"
            return winner
