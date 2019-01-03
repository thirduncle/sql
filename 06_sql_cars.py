import sqlite3

with sqlite3.connect("cars.db") as connection:

	c = connection.cursor()

	#c.execute("""CREATE TABLE inventory
	#			(Make TEXT, Model TEXT, Quantity INT)
	#			""")

	cars = [
			('Ford', 'Fiesta', 15),
			('Ford', 'Focus', 12),
			('Ford', 'Fusion', 11),
			('Honda', 'Accord', 15),
			('Honda', 'Civic', 15)
			]

	#c.executemany("INSERT INTO inventory VALUES(?,?,?)", cars)

	#c.execute("UPDATE inventory SET Quantity = 23 WHERE Make = 'Honda'")

	#c.execute("DELETE FROM inventory WHERE Make = 'FORD' OR Make = 'TOYOTA'")

	c.execute("SELECT DISTINCT * FROM inventory WHERE Make = 'Ford'")

	rows = c.fetchall()

	for row in rows:
		print(row)

