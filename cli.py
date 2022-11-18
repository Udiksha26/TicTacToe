# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import TicTacToe


if __name__ == "__main__":
        game = TicTacToe()
        print(" Play against : ")
        print(" 1. Another Person ")
        print(" 2. Bot ")
        choice = int(input(" Choice: "))
        if choice == 1: 
                print("True")
        else:


                False


        if game.is_another_person():
                game.play_with_human()
        else:
                game.play_with_computer()


