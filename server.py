import logic
from urllib import request
from flask import Flask , render_template , url_for , request , redirect
app = Flask(__name__)

game= logic.TicTacToe()
@app.route('/',methods=('GET', 'POST'))
def index ():
    game.board = [[" "," "," "],[" "," "," "],[" "," "," "],]

    game.count = 0

    game.name1 = "DefaultName1",

    game.name2 = "bot",
    if request.method == 'POST':
        name1 = request.form['name1']
        S1 = request.form['options1']
        name2 = request.form['name2']
        print(name1)
        game.player1= name1
        game.player2= name2
        print(name2)
        print(S1)
        choice=S1
        if S1 == "Bot":
            game.choice = 2
        else:
            game.choice = 1
        return redirect(url_for('game'))

    return render_template('assignment9.html')

    



@app.route('/game',methods=('GET', 'POST'))
def game ():
    data = {
        "board": game.board,
        "player1": game.player1,
        "player2" : game.player2,
        "count": game.count,
    }

    return render_template('Game.html',data=data)

@app.route('/user/<username>')
def profile(username):
    return 'Hello ' + username + '!'

@app.route('/user2/<name>')
def name(name):
    return render_template('profile.html', name=name)

