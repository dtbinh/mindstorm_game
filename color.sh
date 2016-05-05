#!/usr/bin/env bash

Sensor1="/sys/class/lego-sensor/sensor0"
echo COL-COLOR > $Sensor1/mode

while true ; do
  color="$( cat $Sensor1/value0 )"
  for value in 2 3 4 5 ; do
    if [ "$color" = "$value" ] ; then
      touch /root/someone_has_won
    fi
  done
  sleep .5
done
