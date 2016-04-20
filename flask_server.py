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
            return render_template('index.html',team=team())
        elif request.form['submit'] == 'left':
            return render_template('index.html',team=team())
        elif request.form['submit'] == 'right':
            return render_template('index.html',team=team())
        elif request.form['submit'] == 'backward':
            return render_template('index.html',team=team())
        else:
            return render_template('index.html',team=team())
    else:
        return render_template('index.html',team=team())
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
