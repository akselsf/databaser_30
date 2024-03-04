import sqlite3

con = sqlite3.connect("db.sqlite3")

cur = con.cursor()

file = open("initialise.sql", "r")

cur.executescript(file.read())

con.close()