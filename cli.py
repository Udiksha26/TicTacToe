# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import TicTacToe
import numpy as np 
import pandas as pd

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
                

 #storing values


game_filename = "gamesdata.csv"
#games dataframe
'''games = pd.DataFrame(columns=[
    "Game Id",
    "Player 1",''
    "Player 2",
    "Winner",
])'''

def read_games():
    try:
        return pd.read_csv("gamesdata.csv")
        
    except FileNotFoundError:
            return pd.DataFrame(columns= [
               "Game Id",
               "Player 1",
               "Player 2",
                "Winner", 
            ])

games = read_games()
print (len(games))

if winning == 'X':
    print("Winning = ", winning, name1)
    games.loc[len(games)] = {
    "Game Id": len(games),
    "Player 1": name1,
    "Player 2": name2,
    "Winner": name1,
}
elif winning == '0':
    print("Winning = ", winning, name2)
    games.loc[len(games)] = {
    "Game Id": len(games),
    "Player 1": name1,
    "Player 2": name2,
    "Winner": name2,
}
    


print("_____________________________")
print(games)
games.to_csv("gamesdata.csv")
print("Done")

  


