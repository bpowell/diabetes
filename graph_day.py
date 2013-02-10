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
		data.append( (row[2], row[1][0:2]) )

	print data

X = [ y for (x,y) in data ]
Y = [ x for (x,y) in data ]

plt.plot( X, Y, ':rs' )
plt.axis([0,24,0,300])
plt.show()
