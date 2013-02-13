#!/usr/bin/env python

import sys

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
            data.append( (row[2], int(row[1][0:2])) )

        self.db.close()

        X = [ y for (x,y) in data ]
        Y = [ x for (x,y) in data ]

        self.g.single_line(X, Y, 'rs', range(0,23), range(20,320,20))
        self.g.title("Glucose levels by time of day.")
        self.g.show()
