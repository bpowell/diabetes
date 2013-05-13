#!/usr/bin/env python

import csv

num_days = raw_input("Enter number of days to add: ")
num_days = int(num_days)

data = []

for day in range(num_days):
	date = raw_input("Enter date: ")

	num_pokes = raw_input("Number of pokes: ")
	num_pokes = int(num_pokes)

	for poke in range(num_pokes):
		t = raw_input("Time: ")
		g = raw_input("Number: ")
		
		data.append([date, t, g, None])

with open('glucose.csv', 'a') as csvfile:
	w = csv.writer(csvfile, delimiter=',', lineterminator='\n')
	for d in data:
		w.writerow(d)
