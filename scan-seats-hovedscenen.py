
with open('hovedscenen.txt', 'r') as file:
    lines = file.readlines()

date = 0

for line in lines:
    # print(line.strip()) 

    if "Dato" in line:
        date = line.split()[1]
    

#Finne parkett seter
sold_seats_parkett = []

rows = lines[::-1]
row_number = 1

for row in rows[0:18]:
    seat_number = 1

    for seat in row.strip():
        if seat == "1":
            sold_seats_parkett.append((row_number, seat_number))

        seat_number+= 1

    row_number+=1

for sold in sold_seats_parkett:
    print(sold)