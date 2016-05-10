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
	def __init__(self, ip, team):
		self.ip = ip
		self.team = team

def check_active(ip_adr):
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
lock = threading.Lock()
def robot_movement(direction):
	if True:
	# Add functions before returning to run commands
		if direction == 'forward':
			# controller.motor is a function which runs the motors for 2 sec
			controller.motor('forward')
		elif direction == 'left':
			controller.motor('left')
		with lock:
			print(threading.current_thread().name, direction)

def worker():
	while True:
		item = q.get()
		robot_movement(item)
		q.task_done()

q = Queue()
for i in range(4):
	t = threading.Thread(target=worker)
	t.daemon = True
	t.start()

players = []
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	print("Running Index")
	address = request.remote_addr
	if check_active(address):
		print('Adding')
		players.append(player(address, team()))
		team_var = get_team(address)
		return render_template('index.html', team=team_var)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	if request.method == 'POST':
		if request.form['submit'] == 'kill':
			controller.kill()
		return render_template('admin.html', info=players)

@app.route('/game', methods=['GET', 'POST'])
def game():
	player_ip = request.remote_addr
	redirect_var = True
	for i in players:
		if player_ip == i.ip:
			print("OK")
			redirect_var = False
	if redirect_var:
		return redirect(url_for('index'))

	team_var = get_team(player_ip)
	direction_var = None
	start = time.perf_counter()
	if request.method == 'POST':
		q.put(request.form['submit'])
	print('time:',time.perf_counter()-start)
	return render_template('game.html',team=team_var, direction=direction_var)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
