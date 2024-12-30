"This is course IN1000 what I learned"
capital_city = {"Sverige":"Stockholm", "Norge":"Oslo"}
land = input("Velg land i nordre Skandinavia: ")
print(capital_city[land])
person = input("Konge: ")
etterkommere = {"Oscar":"Haakon", "Haakon":"Olav", "Olav":"Harald"}

barn = etterkommere[person]
barnebarn = etterkommere[barn]

print("Barnebarn: " + barnebarn)