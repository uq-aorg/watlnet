#!/bin/sh
DATE=$(date +"%Y-%m-%d_%H%M%S")
raspistill -q 20 -t 1500 -vf -hf -o /media/pi/6094-64591/Timelapse/test_$DATE.jpg -n

