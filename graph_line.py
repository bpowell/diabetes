#!/usr/bin/env python

import sys

from database import Database
from graph import Graph

class Graph_Line:
    db = None
    g = None

    def __init__(self):
        self.db = Database()
        self.g = Graph()

    def one_day(self, date):
        self.db.open()
        date = (date,)
        rows = self.db.select('select * from glucose where date=?', date)
        data = [] 

        if rows == None:
            print("Not a valid date. Exiting...")
            self.db.close()
            sys.exit(1)

        for row in rows:
            data.append( (row[2], int(row[1][0:2])) )

        self.db.close()

        X = [ y for (x,y) in data ]
        Y = [ x for (x,y) in data ]

        self.g.single_line( X, Y, ':rs' )
        self.g.title("Glucose levels by time of day on " + date[0])
        self.g.show()
