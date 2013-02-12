#!/usr/bin/env python

from graph_line import Graph_Line
from import_db import import_glucose_csv

import_glucose_csv()
date = raw_input("Input date: ")
g = Graph_Line()
g.one_day(date)
