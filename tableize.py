#!/usr/bin/env python

import csv
import datetime
import sys
import math
import numpy as np

from database import Database

class Tableize:
	db = None
	data = None

	def __init__(self, start_day):
		self.db = Database()
		self.db.open()
		self.start_day = datetime.date(2000+int(start_day[6:]), int(start_day[0:2]), int(start_day[3:5]))
		self.date_delta = datetime.timedelta(days=1)

		self.data = [["date", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, "Average", "Median", "Std Dev"]]
		l = self.db.select('select level from glucose')
		self.levels = []
		for x in l:
			self.levels.append(x[0])

		row = self.get_row()
		while len(row)>0:
			self.data.append(self.create_row(row))
			self.next_date()
			row = self.get_row()

		self.data.append(self.hourly_avg())
		self.data.append(self.hourly_median())
		self.data.append(self.hourly_std_dev())

		with open('table.csv', 'wb') as f:
			w = csv.writer(f)
			w.writerows(self.data)

	def get_row(self):
		return self.db.select('select level, time from glucose where date=? order by time', [self.start_day.strftime("%m/%d/%y")])

	def next_date(self):
		self.start_day += self.date_delta

	def create_row(self, next_row):
		row = []
		row.append(self.start_day.strftime("%m/%d/%y"))

		count = 0
		total = 0

		for i in range(0,24):
			row.append(None)

		lvl = []
		for l,t in next_row:
			row[int(t[0:2])+1]=l
			count += 1
			total += int(l)
			lvl.append(l)

		row.append(total/count)
		row.append(self.median(lvl))
		row.append(self.online_variance(lvl))

		return row

	def hourly_avg(self):
		row = []
		row.append("Average")

		for i in range(24):
			d = [r[i+1] for r in self.data[1:]]
			d = filter(None, d)
			d = map(int, d)

			if len(d)==0:
				row.append(None)
			else:
				row.append(sum(d)/len(d))

		row.append(sum(self.levels)/len(self.levels))

		return row

	def hourly_median(self):
		row = []
		row.append("Median")

		for i in range(24):
			d = [r[i+1] for r in self.data[1:-1]]
			d = filter(None, d)
			d = map(int, d)

			if len(d)==0:
				row.append(None)
			else:
				row.append(self.median(d))

		row.append(None)
		row.append(self.median(self.levels))
		
		return row

	def hourly_std_dev(self):
		row = []
		row.append("Std Dev")

		for i in range(24):
			d = [r[i+1] for r in self.data[1:-2]]
			d = filter(None, d)
			d = map(int, d)

			if len(d)==0:
				row.append(None)
			else:
				row.append(self.online_variance(d))

		row.append(None)
		row.append(None)
		row.append(self.online_variance(self.levels))
		
		return row

	def online_variance(self, a=None):
		d = []
		if a==None:
			a = self.db.select('select level from glucose')
			for x in a:
				d.append(x[0])
		else:
			d = a

		n = 0
		mean = 0
		M2 = 0

		for x in d:
			n = n + 1
			delta  = x - mean
			mean = mean + delta/n
			M2 = M2 + delta*(x-mean)

		if n==1:
			return 0 

		var = M2/(n-1)
		return round(math.sqrt(var), 3)

	def median(self, a):
		m = np.array(a)
		return np.median(m)
