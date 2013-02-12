#!/usr/bin/env python

import sqlite3
import sys
import numpy as np
import matplotlib.pyplot as plt

from database import Database
from graph import Graph

db = Database()
g = Graph()
db.open()
data = []

print("Enter date to graph: ")
date = raw_input("")

date = (date,)

rows = db.select('select * from glucose where date=?', date)

if rows == None:
    print("Not a valid date. Exiting...")
    sys.exit(1)

for row in rows:
    data.append( (row[2], int(row[1][0:2])) )

print data

X = [ y for (x,y) in data ]
Y = [ x for (x,y) in data ]

g.single_line( X, Y, ':rs' )
g.title("Glucose levels by time of day on " + date[0])
g.show()

db.close()
