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
import controller

class player(object):
    def __init__(self, ip, team):
        self.ip = ip
        self.team = team

def check_active(ip_adr):
    print(" ")
    for i in players:
        print(i.ip)

    print(" ")

    if not players == []:
        for i in players:
            if i.ip == ip_adr:
                return False
        else:
            return True
    else:
        return True

def team():
    teams = ['blue', 'red', 'green', 'yellow']
    n = randint(0,3)
    return(teams[n])

def get_team(ip):
    for i in players:
        if ip == i.ip:
            return i.team

players = []
print(players)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    address = request.remote_addr
    if check_active(address):
        print('Adding')
        players.append(player(address, team()))
    team_var = get_team(address)
    return render_template('index.html', info=players, team=team_var)

@app.route('/game', methods=['GET', 'POST'])
def game():
    team_var = get_team(request.remote_addr)
    if request.method == 'POST':
        # Add functions before returning to run commands
        if request.form['submit'] == 'forward':
            # controller.motor is a function which runs the motors for 2 sec
            controller.motor('forward')
            return render_template('game.html',team=team_var, direction='forward')
        elif request.form['submit'] == 'left':
            controller.motor('left')
            return render_template('game.html',team=team_var, direction='left')
        elif request.form['submit'] == 'right':
            controller.motor('right')
            return render_template('game.html',team=team_var, direction='right')
        elif request.form['submit'] == 'backward':
            controller.motor('backward')
            return render_template('game.html',team=team_var, direction='backward')
        else:
            return render_template('game.html',team=team_var, direction='none')
    else:
        return render_template('game.html',team=team_var, direction='none')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
