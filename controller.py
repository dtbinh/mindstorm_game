"""
Functions for controlling the robot over ssh and bash
"""
from time import sleep
import telnetlib, paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ev3dev.local', username='root',password='destroyer')

tn = telnetlib.Telnet('ev3dev.local')
#tn.read_until(b'Password: ')
#tn.write('k'.encode('ascii') + b'\n')
tn.read_until(b"ev3dev login: ")
tn.write('root'.encode('ascii') + b'\n')
tn.read_until(b"Password: ")
tn.write('destroyer'.encode('ascii') + b'\n')
# This is to be able to run one command at a time
# else it will do a new command every time
free = True
tn.write(b'touch test\n')
def kill():
    tn.write(b"beep -f 415.3 -l 300 -n -f 466.16 -l 200 -n -f 369.99 -l 300 -n -f 415.3 -l 800 -n -f 493.88 -l 300 -n -f 466.16 -l 200 -n -f 369.99 -l 300 -n -f 415.3 -l 800" + b"\n")
Sensor1="/sys/class/lego-sensor/sensor0"
ssh.exec_command('echo COL-COLOR > {}/mode'.format(Sensor1))

def team_win(color):
    if color == b'2':
        print("Blue")
        kill()
    elif color == b'3':
        print("Green")
        kill()
    elif color == b'4' and False:
        print("Yellow")
        kill()
    elif color == b'5':
        print("Red")
        kill()
    else:
        print("Not right")
        print(color)
def color():
	stdin, stdout, stderr = ssh.exec_command('cat {}/value0'.format(Sensor1))
	color = stdout._read(1)
	print(color)
	if color in [b'2', b'3', b'4', b'5']:
		team_win(color)

def motor(direction):
	global motor_active
	motor_active = False
	color()
	print(motor_active)
	if not motor_active or True:
		motor_active = True
		print(direction)
		print(b'/root/mindstorm_game/controller.sh ' + direction + b'^]')
		tn.write(b'/root/mindstorm_game/controller.sh ' + direction + b"\n")	
		color()
		motor_active = False
