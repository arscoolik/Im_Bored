import sqlite3

global db
global sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
	uid TEXT,
	brand TEXT,
	size TEXT
	)""")

db.commit()


def reg():
	user_uid = message.from_user.username
	db.commit()
