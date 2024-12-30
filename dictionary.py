
dict_data = {"Name": "A", "year":1995, "place":"Norway", "city": "Oslo"}
# now we add new data items. How to do it?
# for example telephone number{"TP": 44454546}
dict_data["TP"] = 44454546
# How to do update dictionary? for example i want to change city now.we can use update method.
dict_data.update({"city": "Lorenskog"})
print(dict_data)

"""
hovedstad = {"Sverige":"Stockholm", "Norge":"Oslo"}
land = input("Velg land i nordre Skandinavia: ")
print(hovedstad[land])
person = input("Konge: ")
etterkommere = {"Oscar":"Haakon", "Haakon":"Olav", "Olav":"Harald"}

barn = etterkommere[person]
barnebarn = etterkommere[barn]

print("Barnebarn: " + barnebarn)"""