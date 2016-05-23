# mindstorm_game
A game for our Mindstorms robot that we made in class, using ev3dev and Python.

![Image Alt](https://raw.githubusercontent.com/Hackslashloot/mindstorm_game/master/robot.jpg)

## Dependencies:
Python (2 or 3, we had problems with 3 so we switched to 2, but go ahead and try 3 if you want)
Flask
Paramiko
OpenBSD telnet server
ev3dev's Python bindings
A Lego Mindstorms ev3 running ev3dev

## Setup
The robot has two caterpillar tracks with one motor for each, and a color sensor situated in the middle, facing down. The left motor is plugged into port A, the right one is on port B and the color sensor is on port 1.

The web server (flask_server.py) will be run on one of our computers, recieving commands and sending them over to the robot over SSH or telnet, via Bluetooth tethering. SSH is used for color checking, while telnet is used for actual movement. We originally planned to have the robot itself run the web server and act as a Wifi access point to make others able to connect to it, but that proved to be impossible due
to technical limitations, namely lack of working memory and increased power consumption.

Other computers will then connect to the web server and control the robot via a simple web interface. Players will be divided into four teams, each with their own color and base. The objective of the game is to get the robot to your base, while the other players try to drive it to theirs. A real life version of Twitch Plays Pokémon, of sorts.

## What we did
The idea for this project came to our minds when we learned that our school had bought new Mindstorms ev3 robots for technology class, to replace the aging NXT's. When we realised we could run Linux on it, we quickly decided that we would do something else.

We had a pretty clear idea of what we wanted to do from the beginning, but not so much about the robot design. We spent a couple of classes just trying to build something that was robust enough and had room for the color sensor in the middle.

But, of course, that was the easy part. Making the actual program was a lot harder. At first, we had problems with connecting the robot to our computers, and then the color sensor suddenly decided everything was blue. But in the end we managed to make something largely operational, and we managed to showcase our project and actually test the game under real-life conditions.

The test did unfortunately not go that well. Half of our classmates recieved error messages when trying to connect to the web server, and those who managed to get in couldn't control the robot very well as it didn't accept any commands when it was moving. No team managed to win, but in the end, the color sensor decided everything was blue again and the robot played the theme of pro wrestler John Cena through its rudimentary speaker.

So all in all, our project went well and was very fun doing. We learned many things during the project, like the basics of Python and multithreading. We will most definitely have use for these skills in the future.

## TODO:
1. Make the server/robot not crash with multiple people controlling it.
2. Motor controlling for multiple people
