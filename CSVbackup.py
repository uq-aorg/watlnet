#!/usr/bin/python
from datetime import datetime
import os
import pymysql
import csv
os.chdir("/media/pi/6094-64591/DataBackUp")

#filename=open('test.csv','a')
#c=csv.writer(filename)

filename = datetime.now().strftime("%Y%m%d-%H%M%S")
file=open(filename + '.csv','w')
c=csv.writer(file)

conn = pymysql.connect(user='root', password='Australia57',
                              host='localhost',
                              database='WeatherData')


cursor = conn.cursor()

query = ("SELECT Temperature, Humidity, DewPoint from Temperature_Humidity")

cursor.execute(query)

for Temperature, Humidity, DewPoint in cursor:
    c.writerow([Temperature,Humidity,DewPoint] )
    
    

cursor.close()
#filename.close()
file.close()
conn.close()
os.chdir("/home/pi")
