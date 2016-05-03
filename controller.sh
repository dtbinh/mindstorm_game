#!/usr/bin/env bash

MotorA="/sys/class/tacho-motor/motor1"
MotorB="/sys/class/tacho-motor/motor2"
echo reset > $MotorA/command > $MotorB/command
echo coast > $MotorA/stop_action > $MotorB/stop_action
echo 2000 > $MotorA/time_sp > $MotorB/time_sp

trap "read -s" SIGINT

while true ; do
  read -n 1 -s command
  if [[ "$command" == "f" ]] ; then
    echo 50 > $MotorA/speed_sp > $MotorB/speed_sp
    echo run-timed > $MotorA/command > $MotorB/command
  elif [[ "$command" == "b" ]] ; then
    echo -50 > $MotorA/speed_sp > $MotorB/speed_sp
    echo run-timed > $MotorA/command > $MotorB/command
  elif [[ "$command" == "l" ]] ; then
    echo 50 > $MotorA/speed_sp
    echo -50 > $MotorB/speed_sp
    echo run-timed > $MotorA/command > $MotorB/command
  elif [[ "$command" == "r" ]] ; then
    echo -50 > $MotorA/speed_sp
    echo 50 > $MotorB/speed_sp
    echo run-timed > $MotorA/command > $MotorB/command
  fi
done
