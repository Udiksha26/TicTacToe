# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.



import random


class TicTacToe:

    game_type = {1: "Another Person", 2: "Computer"}
    human_players = {True: "Player 1 (0)", False: "Player 2 (X)"}

    def __init__(self) -> None:
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def is_another_person(self):
        print(" Play against : ")
        print(" 1. Another Person ")
        print("  2. Bot ")
        self.choice = int(input(" Choice : "))
        return True if self.choice == 1 else False

    def print_board(self):
        """Print the game board. 
        
        #     """
       
        for row in self.board:
            print(*row)

    def check_win(self, win_char):
        board = self.board
        if board[0][0] == board[0][1] == board[0][2] == win_char: #Checking rows
            return win_char
        elif board[1][0] == board[1][1] == board[1][2] == win_char:
            return win_char
        elif board[2][0] == board[2][1] == board[2][2] == win_char:
            return win_char
        elif board[0][0] == board[1][0] == board[2][0] == win_char: #checking columns
            return win_char
        elif board[0][1] == board[1][1] == board[2][1] == win_char:
            return win_char
        elif board[0][2] == board[1][2] == board[2][2] == win_char:
            return win_char
        elif board[1][1] == board[2][2] == board[0][0] == win_char:  #checking diagonals
            return win_char
        elif board[0][2] == board[1][1] == board[2][0] == win_char:
            return win_char
        else:
            return None

    def get_computer_move(self):
        board = self.board
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] != None:
            self.get_computer_move()
        else:
            board[row][column] = "O"
            return board

    def play_with_human(self):
        winner = None
        turn = True
        move_number = 0
        while move_number < 9 and winner == None:
            print(f"Take a turn {self.human_players[turn]}!")

            # Show the board to the user
            self.print_board()

            # Input a move from the player
            row = int(input("Enter the row number (0-2) : "))
            column = int(input("Enter the column number (0-2) : "))

            # Do not allow players to play the same square
            if self.board[row][column] != None:
                print("Please play the move in an empty square!")
                continue

            if turn:
                self.board[row][column] = "X"
                winner = self.check_win("X")
            else:
                self.board[row][column] = "O"
                winner = self.check_win("O")

            # Increment the number of moves played
            move_number += 1
            # Update who's turn it is
            turn = not turn

        if winner == None:
            print("Draw")
        else:
            print(f"{self.human_players[not turn]} is the winner!! ")

    def play_with_computer(self):
        move_number = 0
        while move_number < 9:
            print(f"--------Take a turn Player!-----------")

            # Show the board to the user
            self.print_board()

            # Input a move from the player
            row = int(input("Enter the row number (0-2) : "))
            column = int(input("Enter the column number (0-2) : "))

            # Do not allow players to play the same square
            if self.board[row][column] != None:
                print("Please play the move in an empty square!")
                continue

            self.board[row][column] = "X"
            if self.check_win("X"):
                print("****Congratulations You Win!****")
                return

            self.get_computer_move()

            if self.check_win("X"):
                print("You lost! Better luck next time. :( ")
                return

            # Increment the number of moves played
            move_number += 2