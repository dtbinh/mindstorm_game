#!/usr/bin/env bash

MotorA="/sys/class/tacho-motor/motor1"
MotorB="/sys/class/tacho-motor/motor2"
echo reset > $MotorA/command > $MotorB/command
echo coast > $MotorA/stop_command > $MotorB/stop_command
echo 2000 > $MotorA/time_sp > $MotorB/time_sp

echo "PID: $$"

trap "read" SIGINT

while true ; do
  read -n 1 command
  if [[ "$command" == "f" ]] ; then
    echo 50 > $MotorA/duty_cycle_sp > $MotorB/duty_cycle_sp
    echo run-timed > $MotorA/command > $MotorB/command
  elif [[ "$command" == "b" ]] ; then
    echo -50 > $MotorA/duty_cycle_sp > $MotorB/duty_cycle_sp
    echo run-timed > $MotorA/command > $MotorB/command
  elif [[ "$command" == "l" ]] ; then
    echo 50 > $MotorA/duty_cycle_sp
    echo -50 > $MotorB/duty_cycle_sp
    echo run-timed > $MotorA/command > $MotorB/command
  elif [[ "$command" == "r" ]] ; then
    echo -50 > $MotorA/duty_cycle_sp
    echo 50 > $MotorB/duty_cycle_sp
    echo run-timed > $MotorA/command > $MotorB/command
  fi
done
