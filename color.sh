#!/usr/bin/env bash

Sensor1="/sys/class/lego-sensor/sensor0"
echo COL-COLOR > $Sensor1/mode

while true ; do
  color="$( cat $Sensor1/value0 )"
  for value in 2 3 4 5 ; do
    if [ "$color" = "$value" ] ; then
      beep -f 415.3 -l 300 -n -f 466.16 -l 200 -n -f 369.99 -l 300 -n -f 415.3 -l 800 -n -f 493.88 -l 300 -n -f 466.16 -l 200 -n -f 369.99 -l 300 -n -f 415.3 -l 800
      sleep 3.2
    fi
  done
  #sleep .5
done
