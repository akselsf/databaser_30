

import sqlite3

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

# konstanter
teater_navn = "Trøndelag Teater"

# Direktør og teater
cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES('Elisabeth Egseth Hansen', 'teatersjef@trondelag-teater.no', 'fast');")
cur.execute("INSERT INTO teater (navn, direktoer_id) VALUES (?, ?);", (teater_navn, str(cur.lastrowid)))

# Sal 
cur.execute("INSERT INTO sal (navn, teater_navn) VALUES (?, 'Hovedscenen');", (teater_navn,))
cur.execute("INSERT INTO sal (navn, teater_navn) VALUES (?, 'Gamle Scene');", (teater_navn,))

# Områder - Hovedscenen
cur.execute("INSERT INTO omraade (navn, sal_navn, teater_navn) VALUES ('Parkett', ?, ?);", ("Hovedscenen", teater_navn))
cur.execute("INSERT INTO omraade (navn, sal_navn, teater_navn) VALUES ('Galleri', ?, ?);", ("Hovedscenen", teater_navn))
# Områder - Gamle Scene
cur.execute("INSERT INTO omraade (navn, sal_navn, teater_navn) VALUES ('Galleri', ?, ?);", ("Gamle Scene", teater_navn))
cur.execute("INSERT INTO omraade (navn, sal_navn, teater_navn) VALUES ('Balkong', ?, ?);", ("Gamle Scene", teater_navn))
cur.execute("INSERT INTO omraade (navn, sal_navn, teater_navn) VALUES ('Parkett', ?, ?);", ("Gamle Scene", teater_navn))

# Rader
# Hovedscenen - parkett
for i in range(1, 19):
    cur.execute("INSERT INTO rad (rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, 'Parkett', 'Hovedscenen', ?);", (i, teater_navn))
# Hovedscenen - galleri
for i in range(1, 5):
    cur.execute("INSERT INTO rad (rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, 'Galleri', 'Hovedscenen', ?);", (i, teater_navn))
# Gamle Scene - Parkett
for i in range(1, 11):
    cur.execute("INSERT INTO rad (rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, 'Parkett', 'Gamle Scene', ?);", (i, teater_navn))
# Gamle scene - Balkong
for i in range(1, 5):
    cur.execute("INSERT INTO rad (rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, 'Balkong', 'Gamle Scene', ?);", (i, teater_navn))
# Gamle Scene - Galleri
for i in range(1, 4):
    cur.execute("INSERT INTO rad (rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, 'Galleri', 'Gamle Scene', ?);", (i, teater_navn))

# Seter
# Hovedscenen - parkett
for i in range(1, 449):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Parkett', 'Hovedscenen', ?);", (i, (i//29) + 1, teater_navn))
for i in range(449, 467):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Parkett', 'Hovedscenen', ?);", (i, 17, teater_navn))
for i in range(471, 477):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Parkett', 'Hovedscenen', ?);", (i, 17, teater_navn))
for i in range(477, 495):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Parkett', 'Hovedscenen', ?);", (i, 18, teater_navn))
for i in range(499, 505):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Parkett', 'Hovedscenen', ?);", (i, 18, teater_navn))

# Hovedscenen - galleri
for i in range(505, 510):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Galleri', 'Hovedscenen', ?);", (i, 1, teater_navn))
for i in range(510, 515):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Galleri', 'Hovedscenen', ?);", (i, 2, teater_navn))
for i in range(515, 520):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Galleri', 'Hovedscenen', ?);", (i, 3, teater_navn))
for i in range(520, 525):
    cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Galleri', 'Hovedscenen', ?);", (i, 4, teater_navn))

# Gamle Scene - Parkett
seterparader = [18,16,17,18,18,17,18,17,17,14]
for i in range(1, 11):
    for j in range(1, seterparader[i-1]+1):
        cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Parkett', 'Gamle Scene', ?);", (j, i, teater_navn))

# Gamle Scene - Balkong
seterparader = [28, 27, 22, 17]
for i in range(1, 5):
    for j in range(1, seterparader[i-1]+1):
        cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Balkong', 'Gamle Scene', ?);", (j, i, teater_navn))
# Gamle Scene Galleri
seterparader = [33, 18, 17]
for i in range(1, 4):
    for j in range(1, seterparader[i-1]+1):
        cur.execute("INSERT INTO sete (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) VALUES (?, ?, 'Galleri', 'Gamle Scene', ?);", (j, i, teater_navn))

# Teaterstykker 
storstavaltnavn = "Størst av alt er kjærligheten"
cur.execute("INSERT INTO Teaterstykke (navn, teater_navn) VALUES ('Kongsemnene', ?);", (teater_navn,))
cur.execute("INSERT INTO Teaterstykke (navn, teater_navn) VALUES (?, ?);", (storstavaltnavn, teater_navn,))

# Akter
for i in range(1, 6):
    cur.execute("INSERT INTO Akt (nummer, teaterstykke_navn) VALUES (?, 'Kongsemnene');", (str(i),))

cur.execute("INSERT INTO Akt (nummer, teaterstykke_navn) VALUES ('1', ?);", (storstavaltnavn,))

# Skuespillere

cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('1', 'Arturo Scotti', 'scotti@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('2', 'Ingunn Beate Strige Øyen', 'oyen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('3', 'Hans Petter Nilsen', 'hnilsen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('4', 'Madeleine Brandtzæg Nilsen', 'mnilsen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('5', 'Synnøve Fossum Eriksen', 'eriksen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('6', 'Emma Caroline Deichmann', 'deichmann@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('7', 'Thomas Jensen Takyi', 'takyi@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('8', 'Per Bogstad Gulliksen', 'gulliksen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('9', 'Isak Holmen Sørensen', 'sorensen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('10', 'Fabian Heidelberg Lunde', 'lunde@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('11', 'Emil Olafsson', 'olafsson@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('12', 'Snorre Ryen Tøndel', 'tondel@gmail.com');")

cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('13', 'Sunniva Du Mond Nordal', 'nordal@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('14', 'Jo Saberniak', 'saberniak@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('15', 'Marte M. Steinholt', 'steinholt@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('16', 'Tor Ivar Hagen', 'thagen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('17', 'Trond-Ove Skrødal', 'skrodal@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('18', 'Natalie Grøndahl Tangen', 'ngtangen@gmail.com');")
cur.execute("INSERT INTO Skuespiller (id, navn, epost) VALUES ('19', 'Åsmund Flaten', 'aflaten@gmail.com');")






# Roller

# Roller i Kongsemnene
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Håkon Håkonson', 1, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Dagfinn Bonde', 11, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Jatgeir Skald', 11, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Sigrid', 6, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Ingebjørg', 6, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Baard Bratte', 10, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Skule Jarl', 3, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Inga frå Vartejg', 2, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Paal Flida', 9, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Fru Ragnhild', 4, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Gregorius Jonsson', 8, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Margrete', 5, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Biskop Nikolas', 7, 'Kongsemnene');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Peter', 12, 'Kongsemnene');")


# Roller i Størst av alt er kjærligheten
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Sunniva Du Mond Nordal', '13', 'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Jo Saberniak', '14', 'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Marte M. Steinholt', '15', 'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Tor Ivar Hagen', '16', 'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Trond-Ove Skrødal', '17', 'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Natalie Grøndahl Tangen', '18', 'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO Rolle (navn, skuespiller_id, teaterstykke_navn) VALUES ('Åsmund Flaten', '19', 'Størst av alt er kjærligheten');")


# RolleIAkt

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Håkon Håkonson', '1', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Håkon Håkonson', '1', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Håkon Håkonson', '1', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Håkon Håkonson', '1', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Håkon Håkonson', '1', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Dagfinn Bonde', '11', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Dagfinn Bonde', '11', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Dagfinn Bonde', '11', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Dagfinn Bonde', '11', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Dagfinn Bonde', '11', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Jatgeir Skald', '11', 'Kongsemnene', '4', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Sigrid', '6', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Sigrid', '6', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Sigrid', '6', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Ingebjørg', '6', 'Kongsemnene', '4', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Baard Bratte', '10', 'Kongsemnene', '1', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Skule Jarl', '3', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Skule Jarl', '3', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Skule Jarl', '3', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Skule Jarl', '3', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Skule Jarl', '3', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Inga frå Vartejg', '2', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Inga frå Vartejg', '2', 'Kongsemnene', '3', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Paal Flida', '9', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Paal Flida', '9', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Paal Flida', '9', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Paal Flida', '9', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Paal Flida', '9', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Fru Ragnhild', '4', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Fru Ragnhild', '4', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Gregorius Jonsson', '8', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Gregorius Jonsson', '8', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Gregorius Jonsson', '8', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Gregorius Jonsson', '8', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Gregorius Jonsson', '8', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Margrete', '5', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Margrete', '5', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Margrete', '5', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Margrete', '5', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Margrete', '5', 'Kongsemnene', '5', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Biskop Nikolas', '7', 'Kongsemnene', '1', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Biskop Nikolas', '7', 'Kongsemnene', '2', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Biskop Nikolas', '7', 'Kongsemnene', '3', 'Kongsemnene');")

cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Peter', '12', 'Kongsemnene', '3', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Peter', '12', 'Kongsemnene', '4', 'Kongsemnene');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Peter', '12', 'Kongsemnene', '5', 'Kongsemnene');")


# størst av alt.. roller
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Sunniva Du Mond Nordal', '13', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Jo Saberniak', '14', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Marte M. Steinholt', '15', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Tor Ivar Hagen', '16', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Trond-Ove Skrødal', '17', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Natalie Grøndahl Tangen', '18', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")
cur.execute("INSERT INTO RolleIAkt (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn) VALUES ('Åsmund Flaten', '19', 'Størst av alt er kjærligheten', 1,'Størst av alt er kjærligheten');")


# Forestillinger
datoerkongen = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05', '2024-02-06']
for i in datoerkongen:
    cur.execute("INSERT INTO Forestilling (tidspunkt, teaterstykke_navn, sal_navn, teater_navn) VALUES (?, 'Kongsemnene', 'Hovedscenen', ?);", (i, teater_navn))

datoerstorstavalt = ["2024-02-03", "2024-02-06", "2024-02-07", "2024-02-12", "2024-02-13", "2024-02-14"]
for i in datoerkongen:
    cur.execute("INSERT INTO Forestilling (tidspunkt, teaterstykke_navn, sal_navn, teater_navn) VALUES (?, ?, 'Gamle Scene', ?);", (i, storstavaltnavn, teater_navn))


# Ansatte / AnsattTil
# Kongen
cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Yury Butusov', 'yury.butusov@trondelag-teater.no', 'fast');") 
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, 'Kongsemnene', 'regi og musikkutvelger')", (id,))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Aleksandr Shishkin-Hokusai', 'aleksandr.shishkinhokusai@trondelag-teater.no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, 'Kongsemnene', 'scenografi og kostymedesigner')", (id,))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Eivind Myren', 'eivind.myren@trondelag-teater.no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, 'Kongsemnene', 'lyddesigner')", (id,))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Mina Rype Stokke', 'mina.rype.stokke@trondelag-teater.no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, 'Kongsemnene', 'dramaturgi')", (id,))


# Størst av alt er kjærligheten
cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Johannes Corell Petersen', 'johannes.corell.petersen@trondelag-teater-no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, ?, 'regi')", (id, storstavaltnavn))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('David Gehrt', 'david.gehrt@trondelag-teater-no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, ?, 'scenografi og kostymedesigner')", (id, storstavaltnavn))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Geute Tønder', 'geute.tonder@trondelag-teater-no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, ?, 'musikkansvarlig')", (id, storstavaltnavn))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Magnus Mikaelsen', 'magnus.mikaelsen@trondelag-teater-no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, ?, 'lyddesigner')", (id, storstavaltnavn))

cur.execute("INSERT INTO ansatt (navn, epost, ansattstatus) VALUES ('Kristoffer Spender', 'kristoffer.spender@trondelag-teater-no', 'fast');")
id = cur.lastrowid
cur.execute("INSERT INTO AnsattTil (ansatt_id, teaterstykke_navn, typejobb) VALUES (?, ?, 'dramaturg')", (id, storstavaltnavn))


# Billett 
# Kongsemnene
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (450, 'Ordinær', 'Kongsemnene');")
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (380, 'Honnør', 'Kongsemnene');")
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (280, 'Student', 'Kongsemnene');")
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (420, 'Gruppe 10', 'Kongsemnene');")
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (360, 'Gruppe honnør 10', 'Kongsemnene');")

# Størst av alt er kjærligheten
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (350, 'Ordinær', ?);", (storstavaltnavn,))
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (300, 'Honnør', ?);", (storstavaltnavn,))
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (220, 'Student', ?);", (storstavaltnavn,))
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (220, 'Barn', ?);", (storstavaltnavn,))
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (320, 'Gruppe 10', ?);", (storstavaltnavn,))
cur.execute("INSERT INTO Billett (pris, billettype, teaterstykke_navn) VALUES (270, 'Gruppe honnør 10', ?);", (storstavaltnavn,))


# Kundeprofil -  Standardprofil
cur.execute("INSERT INTO Kundeprofil (navn, telefon, adresse) VALUES ('Gjest', '0', 'Gjest');")

con.commit()
cur.close()