import sqlite3

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()


dato = input('''Skriv inn en dato på formatet "år-måned-dag": ''')

if (len(dato.split("-")) != 3):
    print("Skriv inn på riktig format")


forestillinger = cur.execute(
    '''SELECT Forestilling.teaterstykke_navn, count(SeterTilBestilling.sete_nr)
    FROM Forestilling 
    LEFT JOIN Bestilling ON Forestilling.teaterstykke_navn=Bestilling.forestilling_navn AND date(Forestilling.tidspunkt) = date(Bestilling.forestilling_tidspunkt)
    LEFT JOIN SeterTilBestilling ON Bestilling.id=SeterTilBestilling.bestilling_id
    WHERE date(Forestilling.tidspunkt) = ?
    GROUP BY Forestilling.teaterstykke_navn''', (dato,)).fetchall()


if (len(forestillinger) == 0):
    print("Ingen forestillinger på denne datoen")

else:
    for forestilling in forestillinger:
        print(forestilling[0] + " vises på denne datoen, og har solgt " + str(forestilling[1]) + " sete(r)")



# for forestilling in forestillinger:
#     print(forestilling[1] + " vises denne datoen, og har solgt " + "2" + " billetter")


con.commit()
cur.close()