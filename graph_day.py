#!/usr/bin.env python

import sqlite3
import sys
import numpy as np
import matplotlib.pyplot as plt

conn = None
conn = sqlite3.connect('database.db')
data = []

with conn:
	cur = conn.cursor()
	print("Enter date to graph: ")
	date = raw_input("")

	date = (date,)

	cur.execute('select * from glucose where date=?', date)
	rows = cur.fetchall()

	if rows == None:
		print("Not a valid date. Exiting...")
		sys.exit(1)

	for row in rows:
		data.append( (row[2], int(row[1][0:2])) )

	print data

X = [ y for (x,y) in data ]
Y = [ x for (x,y) in data ]

plt.plot( X, Y, ':rs' )
plt.axis([0,24,0,300])
plt.grid(True)
plt.title("Glucose levels by time of day on " + date[0])
plt.xlabel("Time of day (24HR Time)")
plt.ylabel("Glucose Level")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
plt.yticks([20,40,60,80,100,120,140,160,180,200,220,240,260,280,300])
plt.show()
