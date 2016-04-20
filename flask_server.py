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
from flask import render_template, request, url_for
from random import randint
# This is a local file (game.py) and will probely change name in the near
# future
import game

def team():
    # Replace this function with something that is more permenant
    teams = ['blue', 'red', 'green', 'yellow']
    n = randint(0,3)
    return(teams[n])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Add functions before returning to run commands
        if request.form['submit'] == 'forward':
            motor('forward')
            return render_template('index.html',team=team(), direction='forward')
        elif request.form['submit'] == 'left':
            motor('left')
            return render_template('index.html',team=team(), direction='left')
        elif request.form['submit'] == 'right':
            motor('right')
            return render_template('index.html',team=team(), direction='right')
        elif request.form['submit'] == 'backward':
            motor('backward')
            return render_template('index.html',team=team(), direction='backward')
        else:
            return render_template('index.html',team=team(), direction='none')
    else:
        return render_template('index.html',team=team(), direction='none')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
