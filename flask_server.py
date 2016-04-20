"""
This is the file/script for the webserver which I (Hackslashloot) am in charge
to make, it will be run using flask and Jinja (i think)

TODO:

Use http POST to transfer id and commands?

Template:
HTML
CSS
Other stuff

Flask:
Fix buttons
Unique IDs for everyone

Other:
Team set up
Maybe some kind of controll gui like qt or tkinter for host?
Some easy way to set up how many teams and easy restarts
"""
from flask import Flask
from flask import render_template, request, url_for
from random import randint

def team():
    teams = ['blue', 'red', 'green', 'yellow']
    n = randint(0,3)
    return(teams[n])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'forward':
            return render_template('index.html',team=team())
            #return render_template('index.html',team='forward')
        elif request.form['submit'] == 'left':
            return render_template('index.html',team=team())
            #return render_template('index.html',team='left')
        elif request.form['submit'] == 'right':
            return render_template('index.html',team=team())
            #return render_template('index.html',team='right')
        elif request.form['submit'] == 'backward':
            return render_template('index.html',team=team())
            #return render_template('index.html',team='backward')
        else:
            return render_template('index.html',team=team())
    else:
        return render_template('index.html',team=team())
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
