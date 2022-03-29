import sqlite3


class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file, check_same_thread=False)
		self.cursor = self.connection.cursor()

	def add_check(self, user_id, bill_id, good_id, time):
		with self.connection:
			self.cursor.execute("INSERT INTO 'check' ('user_id', 'bill_id', 'good_id', 'time') VALUES (?,?,?,?)", (user_id, bill_id, good_id, time,))

	def get_check(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM 'check' WHERE user_id = ?", (user_id,)).fetchall()
			if not len(result):
				return False
			return result[0][2:]

	def get_code_75(self):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM '75lir' WHERE id = (SELECT MAX(id) FROM '75lir')").fetchmany(1)
			self.cursor.execute("DELETE FROM '75lir' WHERE id = (SELECT MAX(id) FROM '75lir')")
			return result[0][1]

	def get_75_length(self):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM '75lir'").fetchall()
			return len(result)

	def get_code_100(self):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM '100lir' WHERE id = (SELECT MAX(id) FROM '100lir')").fetchmany(1)
			self.cursor.execute("DELETE FROM '100lir' WHERE id = (SELECT MAX(id) FROM '100lir')")
			return result[0][1]

	def get_check_length75(self):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM 'check' WHERE good_id = 75").fetchall()
			return len(result)

	def get_check_length100(self):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM 'check' WHERE good_id = 100").fetchall()
			return len(result)

	def get_100_length(self):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM '100lir'").fetchall()
			return len(result)

	def delete(self, user_id):
		with self.connection:
			self.cursor.execute("DELETE FROM 'check' WHERE user_id = ?", (user_id, ))
