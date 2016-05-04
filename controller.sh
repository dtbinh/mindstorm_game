#!/usr/bin/env bash

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
