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
                print("True hbmb")
                name1=input("Enter Player1 name")
                name2=input("Enter Player2 name")
                winning = game.play_with_human()
                print(winning)
                
        else:
                name1=input("Player1 Enter name")
                name2=input("Enter bot name")
              #  game.playing_with_bot()
                winning = game.playing_with_bot()
                print(winning)  
                


  


