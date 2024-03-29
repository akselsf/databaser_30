import sqlite3

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

with open('hovedscenen.txt', 'r') as file:
    lines = file.readlines()

#Finne dato
date = 0

for line in lines:
    if "Dato" in line:
        date = line.split()[1]
    

#Finne parkett seter solgt
sold_seats_parkett = []

rows = lines[::-1]
row_number = 1
seat_number = 1

#Løkke for å iterere over alle rader og alle seter i rad, sjekker om sete har tall 1
for row in rows[0:18]:
    for seat in row.strip():
        if seat == "1":
            #Legger sete med radnummer og setenummer til liste
            sold_seats_parkett.append((row_number, seat_number))

        seat_number+= 1

    row_number+=1

#Lager en bestilling av kundeprofil med telefonnummer 0
cur.execute("INSERT INTO Bestilling (forestilling_navn, forestilling_tidspunkt, kunde_telefon) VALUES ('Kongsemnene', ?,'0');", (date,))

#BestillingsID-en som skal brukes til å kjøpe billetter og seter
order_id = str(cur.lastrowid)

#Kjøper antall billetter tilsvarende antall solgte seter
cur.execute("INSERT INTO BilletterTilBestilling (bestilling_id, billettype, teaterstykke_navn, antall) VALUES (?, 'Ordinær', 'Kongsemnene', ?);", (order_id, len(sold_seats_parkett)))

#Reserverer setene fra den tidligere løkken
for sold in sold_seats_parkett:
    cur.execute("INSERT INTO SeterTilBestilling (bestilling_id, sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, ?, 'Parkett', 'Hovedscenen', 'Trøndelag Teater');", (order_id, sold[1], sold[0]))

con.commit()
cur.close()
file.close()

print("Seter i hovedscenen lagt til i databasen.")