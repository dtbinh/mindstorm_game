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

ssh_color.exec_command('./mindstorm_game/color.sh')

# This is to be able to run one command at a time
# else it will do a new command every time
free = True

def motor(direction):
    if False:
        # The command is a local script that takes startup args
        # We set the variable free to false to make sure that
        # nothing else runs
        #free = False
        ssh_move.exec_command('./mindstorm_game/controller.sh {}'.format(direction))
        #free = True
    ssh_move.exec_command('./mindstorm_game/controller.sh {}'.format(direction))
