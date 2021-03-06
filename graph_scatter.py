#!/usr/bin/env python

import sys
import numpy as np

from database import Database
from graph import Graph

class Graph_Scatter:
    db = None
    g = None

    def __init__(self):
        self.db = Database()
        self.g = Graph()

    def scatter(self):
        self.db.open()
        rows = self.db.select('select * from glucose')
        data = []

        if rows == None:
            print("No data in the database. Something went wrong. Exiting...")
            sys.exit(1)

        for row in rows:
            time = int(row[1][0:2]) + (float(row[1][3:5])/60)
            data.append( (row[2], time) )

        self.db.close()

        X = [ y for (x,y) in data ]
        Y = [ x for (x,y) in data ]

        self.g.axis([0,24,0,320], range(0,23), range(20,320,20))
        self.g.single_line(X, Y, 'rs')
        self.g.title("Glucose levels by time of day.")
        self.g.show()

    def scatter_morning(self):
        self.db.open()
        rows = self.db.select("select * from glucose where time >= '05' and time <='10' + 'ZZZZZ'")
        data = []

        if rows == None:
            print("No data in the database. Something went wrong. Exiting...")
            sys.exit(1)

        for row in rows:
            time = int(row[1][0:2]) + (float(row[1][3:5])/60)
            data.append( (row[2], time) )

        self.db.close()

        X = [ y for (x,y) in data ]
        Y = [ x for (x,y) in data ]

        self.g.axis([5,10,20,320], np.arange(5,10,.25), range(20,320,20))
        self.g.single_line(X, Y, 'rs')
        self.g.title("Glucose levels by time of day.")
        self.g.show()
