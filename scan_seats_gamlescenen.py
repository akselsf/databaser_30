import sqlite3

# Åpne filen det leses fra
with open('gamle-scene.txt', 'r') as file:
    lines = file.readlines()

# Lage en liste over solgte seter
sold_seats = [] # setenr, radnr, område

# Initialisere variabler for å holde styr på hvilket område og rad som leses
curr_area = ""
curr_row = 0
date = lines[0].split(" ")[1]

# Parse file
for i in lines[1:]:
    if i.count("Galleri") == 1:
        curr_area = "Galleri"
        curr_row = 3
    if i.count("Balkong") == 1:
        curr_area = "Balkong"
        curr_row = 4
        
    if i.count("Parkett") == 1:
        curr_area = "Parkett"
        curr_row = 10
        
    if i[0] == "0" or i[0] == "1":
        for j in range(len(i)):
            if i[j] == "1":
         
                sold_seats.append((j+1, curr_row, curr_area))

        curr_row -= 1
file.close()   

# Åpne database og legg til bestilling
con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

# Lage en bestilling med standardprofilen
cur.execute("INSERT INTO Bestilling (forestilling_navn, forestilling_tidspunkt, kunde_telefon) VALUES ('Størst av alt er kjærligheten', ?, ?)", (date, "0"))
order_id = cur.lastrowid

# Legge til billettene til bestillingen
cur.execute("INSERT INTO BilletterTilBestilling (bestilling_id, billettype, teaterstykke_navn, antall) VALUES (?, 'Ordinær', 'Størst av alt er kjærligheten', ?)", (order_id, len(sold_seats)))

# Legge til setene til bestillingen
for i in sold_seats:
    cur.execute("INSERT INTO SeterTilBestilling (bestilling_id, sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, ?, ?, 'Gamle Scene', 'Trøndelag Teater')", (order_id, i[0], i[1], i[2]))

# Commit og lukk
con.commit()
con.close()
