# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

#	create	a	new	database	if	the	database	doesn't	already	exist
conn = sqlite3.connect("new.db")

"""
You	can	also	use	the	 ":memory:" 	string	to	create	a	database	in	memory
only:

conn	=	sqlite3.connect(":memory:")

Keep	in	mind,	though,	that	as	soon	as	you	close	the	connection	the	database	will
disappear.
"""


# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
				(city TEXT, state TEXT, population INT)
				""")

conn.close()