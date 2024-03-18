import sqlite3

con = sqlite3.connect("db2.sqlite3")
cur = con.cursor()

skuespillere_i_stykke = cur.execute('''
    SELECT Teaterstykke.navn, Skuespiller.navn, Rolle.navn
    FROM Teaterstykke 
    INNER JOIN Rolle ON Teaterstykke.navn=Rolle.teaterstykke_navn
    INNER JOIN Skuespiller ON Rolle.skuespiller_id=Skuespiller.id
    ORDER BY Teaterstykke.navn, Skuespiller.navn
    ''').fetchall()

print(f"------------------------------------------------------------------------------------------------------------------------")

for skuespiller in skuespillere_i_stykke:
    print(f"Stykke: {skuespiller[0]:<30} | Skuespiller: {skuespiller[1]:<30} | Rolle: {skuespiller[2]}")
    print(f"------------------------------------------------------------------------------------------------------------------------")

con.commit()
cur.close()