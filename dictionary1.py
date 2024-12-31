"This is course IN1000 what I learned"
"""capital_city = {"Sverige":"Stockholm", "Norge":"Oslo"}
land = input("Velg land i nordre Skandinavia: ")
print(capital_city[land])
person = input("Konge: ")
etterkommere = {"Oscar":"Haakon", "Haakon":"Olav", "Olav":"Harald"}

barn = etterkommere[person]
barnebarn = etterkommere[barn]

print("Barnebarn: " + barnebarn)"""
"This is trix oppgaver 3.04 Fakta om land"
hovedsted = {"Norge": "Oslo", "Nederland": "Amsterdam", "Spania": "Madrid"}
Spraak ={"Norge": "norsk", "Nederland":"nederlandsk",  "Spania":"spansk"}
innbyggerer = {"Norge":5391369, "Nederland":17282163, "Spania":46733038}

"""land = input("velg et land :")
if land in hovedsted:
    print("Hovedsted til", land, "er", hovedsted[land])
    print("I", land, "snakker folk", Spraak[land])
    print(land, "har", innbyggerer[land], "innbyggerere")

else:
    print("Jeg kjenner ikke dette landet!")
"""
#we learn about nested dictionaries 
fakta = {"Norge": {"hovedsted":"Oslo", "Spraak": "norsk", "innbyggerer": 5391369 },
         "Nederland":{"hovedsted":"Amsterdam", "Spraak":"nederlandsk", "innbyggerer":17282163},
         "Spania":{"hovedsted":"Madrid", "Spraak":"spansk", "innbyggerer":46733038},}

land = input("velg et land : ")
if land in fakta:
    print("Hovedsted til", land, "er", fakta[land]["hovedsted"])
    print("I", land, "snakker folk", fakta[land]["Spraak"])
    print(land, "har", fakta[land]["innbyggerer"])
else:
    print("Jeg kjenner ikke dette landet!")
     
