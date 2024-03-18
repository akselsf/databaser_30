import sqlite3  

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

# Get forestilling 
forestilling = cur.execute("SELECT * FROM Forestilling WHERE teaterstykke_navn = 'Størst av alt er kjærligheten' AND tidspunkt = '2024-02-03'").fetchone()

# Get open seats
seats = cur.execute("SELECT * FROM Sete WHERE sal_navn = 'Gamle Scene' AND teater_navn = 'Trøndelag Teater' AND ").fetchall()


