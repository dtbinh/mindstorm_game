#!/usr/bin/env bash

export MotorA="/sys/class/tacho-motor/motor1"
export MotorB="/sys/class/tacho-motor/motor2"
echo reset > $MotorA/command
echo reset > $MotorB/command
echo coast > $MotorA/stop_command
echo coast > $MotorB/stop_command
echo 1000 > $MotorA/time_sp
echo 1000 > $MotorB/time_sp
