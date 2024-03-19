import sqlite3  

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

# Hent forestillingen som skal bestilles billetter til
forestilling = cur.execute("SELECT * FROM Forestilling WHERE teaterstykke_navn = 'Størst av alt er kjærligheten' AND tidspunkt = '2024-02-03'").fetchone()

# Hent alle seter i salen som ikke allerede inngår i en annen bestilling (altså de ledige setene)
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


# Initialisere variabler for å holde styr på de ledige setene i de ulike radene
ticketcount = 9
seats_by_rows = [[] for _ in range(17)]
selected_row = []

# Gå gjennom alle setene og legg til de ledige setene i de ulike radene. Dersom det blir lagt til 9 seter på en rad, avslutt søket og raden settes som den valgte raden
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

# Dersom det ikke er 9 ledige seter på en rad, avbryt bestillingen og gi tilbakemelding til brukeren
if selected_row == []:
    print("Det er desverre ikke 9 ledige plasser på noen rad. Bestilling avbrutt.")
    quit()



# Legg til en ny bestilling med standardbruker
cur.execute("INSERT INTO Bestilling (forestilling_navn, forestilling_tidspunkt, kunde_telefon) VALUES (?, ?, ?)", (forestilling[1], forestilling[0], "0"))
order_id = cur.lastrowid

# Legg til billetter i bestillingen
cur.execute("INSERT INTO BilletterTilBestilling (bestilling_id, billettype, teaterstykke_navn, antall) VALUES (?, 'Ordinær', ?, ?)", (order_id, forestilling[1], ticketcount))

# Legg til setene i bestillingen
for i in selected_row[:9]:
    cur.execute("INSERT INTO SeterTilBestilling (bestilling_id, sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, ?, ?, ?, ?)", (order_id, i[0], i[1], i[2], i[3], i[4]))

# Hent pris for billettene og gi tilbakemelding til brukeren
ticketprice = cur.execute("SELECT pris FROM Billett WHERE teaterstykke_navn = ? AND billettype = 'Ordinær'", (forestilling[1],)).fetchone()
print("Bestilling fullført!")
print("Pris for 9 voksenbilletter: kr", ticketprice[0]*ticketcount)


# Commit og lukk
con.commit()
con.close()
