import sqlite3

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()


forestillinger = cur.execute(
    '''SELECT Forestilling.teaterstykke_navn, Forestilling.tidspunkt, count(SeterTilBestilling.sete_nr)
    FROM Forestilling 
    LEFT JOIN Bestilling ON Forestilling.teaterstykke_navn=Bestilling.forestilling_navn AND date(Forestilling.tidspunkt) = date(Bestilling.forestilling_tidspunkt)
    LEFT JOIN SeterTilBestilling ON Bestilling.id=SeterTilBestilling.bestilling_id
    GROUP BY Forestilling.teaterstykke_navn, Forestilling.tidspunkt
    ORDER BY count(SeterTilBestilling.sete_nr) DESC''').fetchall()

for forestilling in forestillinger:
    print(f"Stykke: {forestilling[0]:<30} | Dato: {forestilling[1]:<10} | Antall solgte billetter: {forestilling[2]}")

con.commit()
cur.close()