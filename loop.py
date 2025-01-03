for i in range(11):
    print("i :", i)
for i in range(0,11):
    print("i :", i)

i = 0
while i != 11:
    print("i :", i)
    i += 1

while i <= 10:
    print("i :", i)
    i += 1

list = ["Sheep", "is", "soft", "animals."]
for ord in list:
    print(ord)
for i in range(len(list)):
    print(list[i])

index = 0
while index < len(list):
    print(list[index])
    index += 1

list = [6, -4, 7, -2, 8, -3, 9, -11]
minimum = list[0]
for i in list:
    if i < minimum:
        minimum = i
print("minimum =", minimum)
list = [6, -4, 7, -2, 8, -3, 9, -11]
maximum = list[0]
for i in list:
    if i > maximum:
        maximum = i
print("maximum =", maximum)

aviser = ["Aftenposten", "VG", "Morgenbladet", "Dagbladet", "Klassekampen"]
for i in aviser:
    print("NewsPaper",i)
for i in range(len(aviser)):
    print(aviser[i])

partall = {10, 8, 6, 4, 2, 0}
for i in partall:
    print("partall : ",i)

kallenavn = {"Roger" : "Roggis", "Magnus" : "Kluten", "Stine" : "Lappen", "Ingeborg" : "Skruen"}

