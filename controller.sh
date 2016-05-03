#!/usr/bin/env bash

MotorA="/sys/class/tacho-motor/motor1"
MotorB="/sys/class/tacho-motor/motor2"
echo reset > $MotorA/command
echo reset > $MotorB/command
echo coast > $MotorA/stop_command
echo coast > $MotorB/stop_command
echo 1000 > $MotorA/time_sp
echo 1000 > $MotorB/time_sp

command="$1"

if [[ "$command" == "forward" ]] ; then
  echo 50 > $MotorA/duty_cycle_sp
  echo 50 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
elif [[ "$command" == "backward" ]] ; then
  echo -50 > $MotorA/duty_cycle_sp
  echo -50 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
elif [[ "$command" == "left" ]] ; then
  echo 50 > $MotorA/duty_cycle_sp
  echo -50 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
elif [[ "$command" == "right" ]] ; then
  echo -50 > $MotorA/duty_cycle_sp
  echo 50 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
fi
