#!/bin/bash
sleep 5
#check for network availability?
# while ! ping -c 1 -W 1 8.8.8.8; do
#     echo "Waiting for 8.8.8.8 - network interface might be down..."
#     sleep 1
# done

(/usr/bin/python3 /home/pi/WatchmanService/main.py >/home/pi/WatchmanService/logs/main_logs.txt 2>&1)