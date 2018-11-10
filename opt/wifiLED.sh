#!/bin/bash

# ping the gateway address
/bin/ping -q -c 1 1.1.1.1 > /dev/null

if [ $? -eq  0 ]
then
  echo "Network active"
  sudo python /opt/wifiLED_yes.py

else
  echo "Network down"
  sudo python /opt/wifiLED_no.py
fi