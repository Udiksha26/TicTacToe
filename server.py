from flask import Flask,render_template
app = Flask(__name__)

@app.get('/')
def index ():
    return ''' 
    <link rel = "stylesheet" href ="/static/style.css">
    <div class = "myclass"> this is azure </div>
    '''


@app.get('/game')
def game ():
    return 'My game will run here!'

@app.route('/user/<username>')
def profile(username):
    return 'Hello ' + username + '!'

@app.route('/user/<name>')
def name(name):
    return render_template('profile.html', name=name)