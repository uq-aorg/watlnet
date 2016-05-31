#!/usr/bin/python3
import os
import sys
import time
import datetime
import subprocess
starttime=time.time()

while True:
	#to test the code in the terminal
	print(datetime.datetime.now())

	subprocess.call("/home/pi/Desktop/Startup/CSVbackup.py", shell=True)
	time.sleep(40 - ((time.time()-starttime) % 40))

