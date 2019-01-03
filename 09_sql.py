import sqlite3


with sqlite3.connect("random_nums.db") as connection:

	c = connection.cursor()

	prompt = """
	Select the operation to perform [1-5]:
	1. Average
	2. Max
	3. Min
	4. Sum
	5. Exit
	"""

	while True:

		x = input(prompt)

		if x in set(["1", "2", "3", "4"]):

			operation =	{1: "avg" , 2: "max", 3:"min" ,	4:"sum" }[int(x)]

			c.execute("SELECT {}(num) from random_numbers".format(operation))

			get = c.fetchall()

			for row in get:
				print(row)

			#print(operation	+ ": %f" % get[0])

		elif x == "5":
			print("Exit")

			break



