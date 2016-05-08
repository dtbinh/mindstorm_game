"""
Functions for controlling the robot over ssh and bash
"""
import paramiko

ssh_move = paramiko.SSHClient()
ssh_color = paramiko.SSHClient()
ssh_move.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_color.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_move.connect('ev3dev.local', username='root',password='destroyer')
ssh_color.connect('ev3dev.local', username='root',password='destroyer')

# This is to be able to run one command at a time
# else it will do a new command every time
free = True

def kill():
    ssh_color.exec_command("beep -f 415.3 -l 300 -n -f 466.16 -l 200 -n -f 369.99 -l 300 -n -f 415.3 -l 800 -n -f 493.88 -l 300 -n -f 466.16 -l 200 -n -f 369.99 -l 300 -n -f 415.3 -l 800")
    ssh_move.exec_command('killall bash')
    quit()

Sensor1="/sys/class/lego-sensor/sensor0"
ssh_color.exec_command('echo COL-COLOR > {}/mode'.format(Sensor1))

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
    stdin, stdout, stderr = ssh_color.exec_command('cat {}/value0'.format(Sensor1))
    color = stdout._read(1)
    print(color)
    if color in [b'2', b'3', b'4', b'5']:
        team_win(color)

def motor(direction):
    color()
    ssh_move.exec_command('./mindstorm_game/controller.sh {}'.format(direction))
    color()
