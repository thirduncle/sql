import sqlite3
import random

with sqlite3.connect("random_nums.db") as connection:
	c = connection.cursor()

	c.execute("DROP TABLE if exists random_numbers ")
	c.execute("CREATE TABLE random_numbers(num INT)")

	for i in range(100):
		c.execute("INSERT INTO random_numbers VALUES(?)", (random.randint(0, 100),))
