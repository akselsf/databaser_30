import sqlite3
con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

print("Finn ut hvilke skuespillere som har spilt i samme akt.")

skuespiller = None
while skuespiller == None:
    skuespillernavn = input("Skriv inn skuespillernavn (eller 'q' for å avslutte): ")
    if skuespillernavn == "q":
        quit()
    skuespiller = cur.execute("SELECT * FROM Skuespiller WHERE navn = ?", (skuespillernavn,)).fetchone()
    if skuespiller == None:
        print("Fant ingen skuespillere med det navnet.")

skuespiller_id = skuespiller[0]
skuespillere = cur.execute('''
    SELECT DISTINCT Skuespiller.navn, RolleIAkt.teaterstykke_navn FROM RolleIAkt 
    INNER JOIN Akt ON Akt.nummer = RolleIAkt.akt_nummer AND Akt.teaterstykke_navn = RolleIAkt.akt_teaterstykke_navn 
    INNER JOIN Skuespiller ON RolleIAkt.skuespiller_id = Skuespiller.id
    WHERE (Akt.nummer, Akt.teaterstykke_navn) IN 
    (SELECT RolleIAkt.akt_nummer, RolleIAkt.akt_teaterstykke_navn FROM RolleIAkt 
    INNER JOIN Rolle ON Rolle.skuespiller_id = ROlleIAkt.skuespiller_id AND Rolle.navn = RolleIAkt.rolle_navn AND RolleIAkt.teaterstykke_navn = Rolle.teaterstykke_navn
    INNER JOIN Skuespiller ON Rolle.skuespiller_id = Skuespiller.id WHERE Skuespiller.id = ?) 
''', (skuespiller_id,)).fetchall()

skuespillere = filter(lambda x: x[0] != skuespillernavn, skuespillere)
print(f"Skuespilleren {skuespillernavn} har spilt i samme akt med følgede skuespillere:")
for skuespiller in skuespillere:
    print(f"{skuespiller[0]} i {skuespiller[1]}")





