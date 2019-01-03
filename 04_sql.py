# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

import csv

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	employees = csv.reader(open("/home/mkir/Documents/Python/RealPython/employees.csv", "rU"))

	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)