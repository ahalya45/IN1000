
dict_data = {"Name": "A", "year":1995, "place":"Norway", "city": "Oslo", "status":"jobless"}
# now we add new data items. How to do it?
# for example telephone number{"TP": 44454546}
dict_data["TP"] = 44454546
# How to do update dictionary? for example i want to change city now.we can use update method.
dict_data.update({"city": "Lorenskog"})
#Removing items(pop(),popitem(), del(), clear())
# we can use pop method removes the item with specified key name
#dict_data.pop("status")
#when we use popitem, it removes the last inserted item
#dict_data.popitem()
#del keyword removes the item with the specified key name
#del dict_data["place"]
#del keyword can also delete the complete dictionary del dict_data
#clear()method empities the dictionary
print(dict_data)
#can we change list order in dictionary order? 
"""No, the contents of a dictionary cannot be sorted in place like that of a list.
However, we can indirectly sort the keys and values of a dictionary by using sorted() function:"""

# How to use for loop in dictionary
for key in dict_data:
    print(key)  #print the key names in the dictionary
    #print(dict_data[key])   #print the key values in the dictionary
for key in dict_data.values():  #here values() method to return values of a dictionary
    print(key)  #
for key in dict_data.keys():  #here keys() method to return keys of a dictionary
    print(key)  #
for key, value in dict_data.items():  #here both keys and values by using items() method to return both keys and values of a dictionary
    print(key, value) 

"Copy a Dictionary" 
#we cannot copy a dictionary dict2 = dict1
# There are ways to make a copy, one way is to use the built in dictinary method and copy()
new_dict = dict_data.copy()

# make a copy is to use the built in function dict()
new_dict = dict(dict_data)
print(new_dict)
"Nested Dictinaries"
# A dictionary can contain dictionaries, is called nested dictionaries
myfamily = {"child1" : {"name" : "Emil", "year" : 2004},
            "child2" : {"name" : "Tobias", "year" : 2007},
            "child3" : {"name" : "Linus", "year" : 2011}} 

# we can create first simple dictionaries and then connected to make anthoer dictionary
child1 = {"name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias", "year" : 2007}
child3 = {"name" : "Linus", "year" : 2011}
myfamily = {"child1" : child1, "child2" : child2,"child3" : child3}
"Access items in Nested Dictinaries"


"""
hovedstad = {"Sverige":"Stockholm", "Norge":"Oslo"}
land = input("Velg land i nordre Skandinavia: ")
print(hovedstad[land])
person = input("Konge: ")
etterkommere = {"Oscar":"Haakon", "Haakon":"Olav", "Olav":"Harald"}

barn = etterkommere[person]
barnebarn = etterkommere[barn]

print("Barnebarn: " + barnebarn)"""