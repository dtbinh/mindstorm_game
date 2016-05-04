"""
Functions for controlling the robot over ssh and bash
"""
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ev3dev.local', username='robot',password='maker')

def motor(direction):
    ssh.exec_command('./{}'.format(direction))
