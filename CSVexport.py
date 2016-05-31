#!/usr/bin/python3
from datetime import datetime
import os
import pymysql
import csv
os.chdir("/media/pi/6094-64591/Data")

filename=open('test.csv','w')
c=csv.writer(filename)

conn = pymysql.connect(user='root', password='Australia57',
                              host='localhost',
                              database='WeatherData')


cursor = conn.cursor()

query = ("SELECT Temperature, Humidity, DewPoint from Temperature_Humidity")


cursor.execute(query)

for Temperature, Humidity, DewPoint in cursor:
    c.writerow([Temperature,Humidity,DewPoint])
    
    

cursor.close()
filename.close()
conn.close()
os.chdir("/home/pi")
