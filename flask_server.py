"""
This is the file/script for the webserver which I (Hackslashloot) am in charge
to make, it will be run using flask and Jinja (i think)

Do you really need to have more info than which button is pressed?

TODO:
Use http POST to transfer id and commands?

Template:
Other stuff

Flask:
Unique IDs for everyone

Other:
Team set up
Maybe some kind of controll gui like qt or tkinter for host?
"""
from flask import Flask
from flask import render_template, request, url_for, make_response
from random import randint
# This is a local file (game.py) and will probely change name in the near
# future
import controller
#import sqlite3

#db_file = sqlite3.connect('database.db')
#db = db_file.cursor()

#db.execute('DROP TABLE players')
#db.execute('CREATE TABLE players (id int, ip text, team text)')

#def new_player(ip, team):
#    count = 1
#    db.execute("INSERT INTO players VALUES (?, ?, ?)", count, str(ip), team)
#    db_file.commit()
#    count += 1

#def get_ip():
#  response = make_response(request.remote_addr)
#  response.mimetype = 'text/plain'
#  return response

def team():
    # Replace this function with something that is more permenant
    teams = ['blue', 'red', 'green', 'yellow']
    n = randint(0,3)
    return(teams[n])

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    team_var = team()
    #print(get_ip())
    #new_player(None, team_var)
    return render_template('index.html', team=team_var)

@app.route('/game', methods=['GET', 'POST'])
def game():
    #team = db.execute("SELECT team FROM players WHERE ip=?", get_ip())
    if request.method == 'POST':
        # Add functions before returning to run commands
        if request.form['submit'] == 'forward':
            controller.motor('forward')
            return render_template('game.html',team=team(), direction='forward')
        elif request.form['submit'] == 'left':
            controller.motor('left')
            return render_template('game.html',team=team(), direction='left')
        elif request.form['submit'] == 'right':
            controller.motor('right')
            return render_template('game.html',team=team(), direction='right')
        elif request.form['submit'] == 'backward':
            controller.motor('backward')
            return render_template('game.html',team=team(), direction='backward')
        else:
            return render_template('game.html',team=team(), direction='none')
    else:
        return render_template('game.html',team=team(), direction='none')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

db_file.close()
