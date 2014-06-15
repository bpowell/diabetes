#!/usr/bin/env python

import csv

num_days = raw_input("Enter number of days to add: ")
num_days = int(num_days)

data = []

date = ""

for day in range(num_days):
        if date == "":
            date = raw_input("Enter date: ")
        else:
            day = int(date[3:5])+1
            if day<10:
                day = "0" + str(day)
            date = date[0:3]+str(day)+date[5:]
            print(date+": correct date?")
            correct = raw_input("Y/n: ")
            if correct=="n":
                date = raw_input("Enter date: ")

	num_pokes = raw_input("Number of pokes: ")
	num_pokes = int(num_pokes)

	for poke in range(num_pokes):
		t = raw_input("Time: ")
		g = raw_input("Number: ")
		
                data.append([date, t[0:2]+':'+t[2:4], g, None])

	print("\n")

with open('glucose.csv', 'a') as csvfile:
	w = csv.writer(csvfile, delimiter=',', lineterminator='\n')
	for d in data:
		w.writerow(d)
