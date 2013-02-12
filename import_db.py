#!/usr/bin/env python

import csv

from database import Database

def import_glucose_csv():
    db = Database()
    db.open()
    db.execute('drop table if exists glucose')
    db.execute('create table glucose(date text, time text, level integer, notes text)')

    with open('glucose.csv', 'rb') as infile:
        dr = csv.DictReader(infile, delimiter=',')
        to_db = [(i['date'], i['time'], i['level'], i['notes']) for i in dr]

    db.executemany("insert into glucose (date, time, level, notes) values (?, ?, ?, ?);", to_db)
    db.commit()
    db.close()
