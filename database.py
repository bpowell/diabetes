#!/usr/bin/env python

import sqlite3
import sys

class Database:
    connection = None
    cursor = None

    def open(self):
        try:
            self.connection = sqlite3.connect('database.db')
            self.cursor = self.connection.cursor()
        except:
            print("Cannot open database. Please create database and try again. Now exiting.")
            sys.exit(1)

    def close(self):
        self.connection.close()

    def execute(self, command, data=None):
        if data!=None:
            self.cursor.execute(command, data)
        else:
            self.cursor.execute(command)

    def executemany(self, command, data=None):
        if data!=None:
            self.cursor.executemany(command, data)
        else:
            self.cursor.executemany(command)

    def select(self, command, data=None):
        if data!=None:
            self.cursor.execute(command, data)
        else:
            self.cursor.execute(command)

        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
