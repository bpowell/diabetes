#!/usr/bin/env python

import sqlite3
import csv

conn = None
conn = sqlite3.connect('database.db')

with conn:
	cur = conn.cursor()
	cur.execute('drop table if exists glucose')

	cmd_create = "create table glucose(date text, time text, level integer, notes text)"
	cur.execute(cmd_create)

	with open('glucose.csv', 'rb') as infile:
		dr = csv.DictReader(infile, delimiter=',')
		to_db = [(i['date'], i['time'], i['level'], i['notes']) for i in dr]
	cur.executemany("insert into glucose (date, time, level, notes) values (?, ?, ?, ?);", to_db)
	conn.commit()

