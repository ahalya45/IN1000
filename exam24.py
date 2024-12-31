
## oppgave 1a
tall = 10
tall =tall +2
print(tall*2)       #svar 24

## oppgave 1b
text1= "1"
text2 = "2"
text3 = "3"
tall = int(text1 +text2) + int(text3)
print(tall)         #svar 15

## oppgave 1c
tall = 9
if tall<10:
    tall = tall+2
    tall = tall+1
else:
    tall = tall -10
print(tall)         #svar 12

## oppgave 1d
summen = 0
for t1 in [1,2]:
    for t2 in [3,4]:
        if t1*t2<4:
            summen += t1*t2
print(summen)       #svar 3

## oppgave 1e
ordbok = {1:2}
teller = 1
while not 5 in ordbok:
    ordbok[1]= ordbok[1]+ teller
    ordbok[ordbok[1]] = teller 
    teller = teller + 1
print(ordbok[1])        #svar 5

## oppgave 2a
class Person:
    def __init__(self, alder):
        self._alder1 = 0
        alder2 = alder      #merk at ikke self
    def sett_alder1(self, alder):
        self._alder1 = alder
    def sett_alder3(self, alder):
        alder3 = alder      #merk at ikke self
    def hent_alder1(self):
        return self._alder1
    def hent_alder2(self):
        return alder2       #merk at ikke self
    def hent_alder3(self):
        return alder3      #merk at ikke self        
    
p1 = Person(10)
p2 = Person(20)
print(p1.hent_alder1())
# Oppgave 2b
tall = p1.hent_alder1()
p3 = p1
p3.sett_alder1(15)
print(tall)

# Exercise 3a
def jages(dyreliste:list[str]):
    #dyreliste = ["mouse", "cat", "dog"]

    if "dog" in dyreliste and "cat" in dyreliste:
        return True
    if "cat" in dyreliste and "mouse" in dyreliste:
        return True
    else:
        return False
assert jages(["cat", "mouse"])
assert not jages(["mouse", "mouse", "dog"])

# Exercise 3b
def utvidet_jages(dyreliste:list, jaging:dict):
    for find in jaging.keys():
        if find in dyreliste and jaging[find] in dyreliste:
            return True
        else:
            return False
assert utvidet_jages(["wolf","mouse", "sheep"],{"wolf": "sheep"})
assert not utvidet_jages(["wolf","mouse","dog"],{"wolf": "sheep","cat": "mouse"})

# Exercise 3c
def flertall(dyreliste:list):
    max = 0
    animal = "uavgjort"
    for dyr in set(dyreliste):      #
        teller = dyreliste.count(dyr)
        if teller > max:
            max = teller
            animal = dyr
        elif teller == max:
            animal = "uavgjort"
    return animal 
assert flertall(["wolf","wolf", " sau"])== "ulv"
assert flertall(["wolf","wolf", " sau","sau"]) == "uavgjort"




    