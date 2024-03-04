import sqlite3

file = open("database.sql", "r")

con = sqlite3.connect("db.db")

cur = con.cursor()
print(file.read())
cur.executescript(file.read())