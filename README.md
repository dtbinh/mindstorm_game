# mindstorm_game
A game for our Mindstorms robot that we made in class, using ev3dev and Python.

## Dependencies:
Python (2 or 3, we had problems with 3 so we switched to 2, but go ahead and try 3 if you want)
Flask
Paramiko
Telnet on the robot
ev3dev's Python bindings
A Lego Mindstorms ev3 running ev3dev

## Setup
The robot has two caterpillar tracks with one motor for each, and a color sensor situated in
the middle, facing down.
The left motor is plugged into port A, the right one is on port B and the color sensor is on
port 1.

We have added telnet because it's faster then SSH. You need to setup telnet manually

The web server (flask_server.py) will be run on one of our computers, recieving commands
and sending them over to the robot over SSH and telnet, via Bluetooth tethering. We originally planned to have the robot itself run the
web server and act as a Wifi access point to make others able to connect to it, but that proved to be impossible due
to technical limitations, namely lack of working memory and increased power consumption.

Other computers will then connect to the web server and control the robot via a simple web
interface. Players will be divided into four teams, each with their own color and base. The
objective of the game is to get the robot to your base, while the other players try to drive
it to theirs. A real life version of Twitch Plays Pokémon, of sorts.

## TODO:
1. Make the server/robot not crash with multiple people controlling it.
2. Motor controlling for multiple people
