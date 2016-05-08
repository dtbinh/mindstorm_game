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
    elif color == b'4':
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
    if color in ['2', '3', '4', '5']:
        team_win(color)

def motor(direction):
    motor_active = False
    global motor_active
    color
    if not motor_active:
        motor_active = True
        ssh_move.exec_command('./mindstorm_game/controller.sh {}'.format(direction))
        color()
        motor_active = False
