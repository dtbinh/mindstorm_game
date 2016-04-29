# mindstorm_game
Mindstorm game using ev3dev and python2

## Dependecies:
Python 2 or 3 (We had problems with 3 so we switched to 2, but you can try)  
Flask  
ev3dev python  
An Lego Mindstorms ev3 with ev3dev  

## Setup/Robot
The robot has two tracks with one motor for each track and a color sensor directed down
in the middle.
Left motor in outA and Right motor in OutB, sensor in In1

Right now the robot will be run from a computer hosting the webserver(flask_server.py)
and sending command over ssh to the robot which will be connected via bluetooth to be able to
run the motors and the color sensor.

You can run the game from the robot, but it only has like 64mb RAM, so it's not ideal

## TODO:
1. Fix the color sensor, it's not working at all.
2. Redirection for the the lobby on the website.
3. Motor controlling for multiple people
4. CSS for lobby/index.html
