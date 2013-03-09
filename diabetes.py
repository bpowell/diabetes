#!/usr/bin/env python

from graph_scatter import Graph_Scatter
from graph_line import Graph_Line
from import_db import import_glucose_csv
from tableize import Tableize

import_glucose_csv()

a = Tableize("01/24/13")

#date = raw_input("Input date: ")
#l = Graph_Line()
#l.one_day(date)
#s = Graph_Scatter()
#s.scatter()
#s.scatter_morning()
