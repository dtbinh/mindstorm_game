"""
This is the file/script for the webserver which I (Hackslashloot) am in charge
to make, it will be run using flask and Jinja (i think)

TODO:

Template:
HTML
CSS
Other stuff

Flask:
Fix buttons
Uniqe IDs for everyone

Other:
Team set up
Maybe some kind of controll gui like qt or tkinter for host?
Some easy way to set up how many teams and easy restarts
"""
from flask import flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
