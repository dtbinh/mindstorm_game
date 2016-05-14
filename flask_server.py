"""

TODO:

Template:
CSS

Flask:

Other:
Team set up
"""
from flask import Flask
from flask import render_template, request, url_for, make_response, redirect
from random import randint
from queue import Queue
import controller, threading, time

class player(object):
	# Small class to carry information to webpage
	def __init__(self, ip, team):
		self.ip = ip
		self.team = team

def check_active(ip_adr):
	# ip_adr is the ip adress of user
	# It returns False if the users ip is already in the list
	if not players == []:
		for i in players:
			if i.ip == ip_adr:
				return False
		else:
			return True
	else:
		return True
def team():
	# This is to give a team, it would be nice to make this
	# assign so it would be even
	teams = ['blue', 'red', 'green', 'yellow']
	n = randint(0,3)
	return(teams[n])

def get_team(ip):
	# k
	for i in players:
		if ip == i.ip:
			return i.team
lock = threading.Lock()
def robot_movement(direction):
	start = time.perf_counter()
	motor_active = False
	if True:
        # All this with motor_active does'nt work
	# Add functions before returning to run commands
		if direction == 'forward' and not motor_active:
			# controller.motor is a function which runs the motors for 2 sec
			motor_active = True
			controller.motor(b'forward')
			motor_active = False
		elif direction == 'left'and not motor_active:
			motor_active = True
			controller.motor(b'left')
			motor_active = False
		elif direction == 'right' and not motor_active:
			motor_active = True
			controller.motor(b'right')
			motor_active = False
                elif direction == 'backward' and not motor_active:
                        motor_active = True
                        controller.motor(b'backward')
                        motor_active = False
		# Multithreading
                with lock:
                        print(time.perf_counter() - start)
                        print(threading.current_thread().name, direction)

def worker():
        # Multithreading
	while True:
		item = q.get()
		robot_movement(item)
		q.task_done()
# Multithreading
q = Queue()
for i in range(16):
	t = threading.Thread(target=worker)
	t.daemon = True
	t.start()

players = []
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        # Lobby
	print("Running Index")
	address = request.remote_addr
	if check_active(address):
		# Addes players to the player list which contanains
                # ip addres and team
                print('Adding')
		players.append(player(address, team()))
		team_var = get_team(address)
	return render_template('index.html', team=team_var)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	# Addon to index with list of ips and a kill button
        if request.method == 'POST':
		if request.form['submit'] == 'kill':
			controller.kill()
		return render_template('admin.html', info=players)

@app.route('/game', methods=['GET', 'POST'])
def game():
        # Controller page
	time_full = time.perf_counter()
	player_ip = request.remote_addr
        # To redirect players who isent in the ip list and has thearfor ni team
	redirect_var = True
	for i in players:
		if player_ip == i.ip:
			print("OK")
			redirect_var = False
	if redirect_var:
		return redirect(url_for('index'))
	team_var = get_team(player_ip)
	direction_var = None
	if request.method == 'POST':
                # Adds a request to move the robot in the multithread queue
		q.put(request.form['submit'])
	print(time.perf_counter() - time_full)
	return render_template('game.html',team=team_var, direction=direction_var)

if __name__ == '__main__':
        # Runs the server, if you should play the game, remove debug option
	app.run(debug=True, host='0.0.0.0')
