import sqlite3  

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

# Get forestilling 
forestilling = cur.execute("SELECT * FROM Forestilling WHERE teaterstykke_navn = 'Størst av alt er kjærligheten' AND tidspunkt = '2024-02-03'").fetchone()

# Get open seats
seats = cur.execute('''
                    SELECT Sete.sete_nr, Sete.rad_nr, Sete.omraade_navn, Sete.sal_navn, Sete.teater_navn FROM Sete WHERE Sete.sal_navn = ? EXCEPT
SELECT Sete.sete_nr, Sete.rad_nr, Sete.omraade_navn, Sete.sal_navn, Sete.teater_navn
FROM Sete
INNER JOIN SeterTilBestilling ON
    Sete.sete_nr = SeterTilBestilling.sete_nr AND
    Sete.rad_nr = SeterTilBestilling.rad_nr AND
    Sete.omraade_navn = SeterTilBestilling.omraade_navn AND
    Sete.sal_navn = SeterTilBestilling.sal_navn AND
    Sete.teater_navn = SeterTilBestilling.teater_navn INNER JOIN Bestilling ON Bestilling.id = SeterTilBestilling.bestilling_id WHERE Bestilling.forestilling_navn = 'Størst av alt er kjærligheten' AND Bestilling.forestilling_tidspunkt LIKE '2024-02-03%'
    ORDER BY Sete.omraade_navn, Sete.rad_nr            
''', (forestilling[2],)).fetchall()

# Sort seats by rows
ticketcount = 9
seats_by_rows = [[] for x in range(17)]
selected_row = []



for i in seats:
    if (i[2] == 'Galleri'):
        seats_by_rows[i[1]-1+14].append(i)
        if len(seats_by_rows[i[1]-1+14]) >= ticketcount:
            selected_row = seats_by_rows[i[1]-1+14]
            break
    if (i[2] == 'Balkong'):
        seats_by_rows[i[1]-1+10].append(i)
        if len(seats_by_rows[i[1]-1+10]) >= ticketcount:
            selected_row = seats_by_rows[i[1]-1+10]
            break
    if (i[2] == 'Parkett'):
        seats_by_rows[i[1]-1].append(i)
        if len(seats_by_rows[i[1]-1]) >= ticketcount:
            selected_row = seats_by_rows[i[1]-1]
            break

if selected_row == []:
    print("Det er desverre ikke 9 ledige plasser på noen rad. Bestilling avbrutt.")
    quit()



# Insert order
cur.execute("INSERT INTO Bestilling (forestilling_navn, forestilling_tidspunkt, kunde_telefon) VALUES (?, ?, ?)", (forestilling[1], forestilling[0], "0"))
order_id = cur.lastrowid
cur.execute("INSERT INTO BilletterTilBestilling (bestilling_id, billettype, teaterstykke_navn, antall) VALUES (?, 'Ordinær', ?, ?)", (order_id, forestilling[1], ticketcount))
for i in selected_row[:9]:
    print(i)
    cur.execute("INSERT INTO SeterTilBestilling (bestilling_id, sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, ?, ?, ?, ?)", (order_id, i[0], i[1], i[2], i[3], i[4]))

ticketprice = cur.execute("SELECT pris FROM Billett WHERE teaterstykke_navn = ? AND billettype = 'Ordinær'", (forestilling[1],)).fetchone()
print("Bestilling fullført!")
print("Pris for 9 voksenbilletter: kr", ticketprice[0]*ticketcount)



con.commit()
con.close()
