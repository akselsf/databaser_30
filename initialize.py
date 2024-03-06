import sqlite3

con = sqlite3.connect("db2.sqlite3")

cur = con.cursor()

file = open("initialize.sql", "r")

cur.executescript(file.read())

con.close()