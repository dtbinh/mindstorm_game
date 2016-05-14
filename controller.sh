#!/usr/bin/env bash

if [[ -f /root/.moving ]] ; then
  exit
fi

MotorA="/sys/class/tacho-motor/motor0"
MotorB="/sys/class/tacho-motor/motor1"
echo reset > $MotorA/command
echo reset > $MotorB/command
echo coast > $MotorA/stop_command
echo coast > $MotorB/stop_command
echo 1000 > $MotorA/time_sp
echo 1000 > $MotorB/time_sp

command="$1"

if [[ "$command" == "forward" ]] ; then
  touch /root/.moving
  echo 50 > $MotorA/duty_cycle_sp
  echo 50 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
  sleep 1
  rm /root/.moving
elif [[ "$command" == "backward" ]] ; then
  touch /root/.moving
  echo -50 > $MotorA/duty_cycle_sp
  echo -50 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
  sleep 1
  rm /root/.moving
elif [[ "$command" == "left" ]] ; then
  touch /root/.moving
  echo 30 > $MotorA/duty_cycle_sp
  echo -30 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
  sleep 1
  rm /root/.moving
elif [[ "$command" == "right" ]] ; then
  touch /root/.moving
  echo -30 > $MotorA/duty_cycle_sp
  echo 30 > $MotorB/duty_cycle_sp
  echo run-timed > $MotorA/command
  echo run-timed > $MotorB/command
  sleep 1
  rm /root/.moving
fi
