#!/usr/bin/env python

import csv
import datetime
import sys

from database import Database

class Tableize:
    db = None
    data = None

    def __init__(self, start_day):
        self.db = Database()
        self.db.open()
        self.start_day = datetime.date(2000+int(start_day[6:]), int(start_day[0:2]), int(start_day[3:5]))
        self.date_delta = datetime.timedelta(days=1)

        self.data = [["date", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, "Average"]]

        row = self.get_row()
        while len(row)>0:
            self.data.append(self.create_row(row))
            self.next_date()
            row = self.get_row()

        self.data.append(self.hourly_avg())

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

        for l,t in next_row:
            row[int(t[0:2])+1]=l
            count += 1
            total += int(l)

        row.append(total/count)

        return row

    def hourly_avg(self):
        row = []
        row.append("Average")

        for i in range(25):
            d = [row[i+1] for row in self.data[1:]]
            d = filter(None, d)
            d = map(int, d)

            if len(d)==0:
                row.append(None)
            else:
                row.append(sum(d)/len(d))

        return row
