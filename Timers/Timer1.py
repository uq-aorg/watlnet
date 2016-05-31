#!/usr/bin/python3
import os
import sys
import time
import datetime
import subprocess
starttime=time.time()
#starttime=datetime.datetime()
while True:
	#to test the code in the terminal
	print(datetime.datetime.now())

	subprocess.call("/home/pi/Desktop/Startup/SHT15bis.py", shell=True)
	time.sleep(4 - ((time.time()-starttime) % 4))
