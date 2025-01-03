# 5.01 lesing fra fil
# Use open() to open name.txt in the Python program
file = open ("navn.txt", "r")

#Create an empty list of names namelist
namelist = []

# Write a loop that goes through the file, 
# line by line, and puts the lines into the list.
for linje in file:
    namelist.append(linje)
file.close()

#5.05 Tabulære filer
# write a function read_car(filename)
# create an empty dictionary as result
"""1.go through the file  
       2.split each line into two columns after ":" (colon).
       3. Also make sure that the newline is removed.
       4. split the string of number of points on "," (comma). 
          This results in a list.
       5.insert the data into the dictionary points, 
       where name is the key and the list of points of the person is the corresponding value.
       6.return the dictionary."""
def read_car(filename):
    result = {}
    for line in open(filename):
        line = line.strip()
        colum = line.split(":")
        key = colum[0]
        value = colum[1]
        result [key] = value
    return result
print(read_car("bil.txt"))

def read_song_contest(filename):
    years = []
    countries = []
    for line in open(filename):
        line = line.strip()
        colum = line.split()
        years.append(colum[0])
        countries.append(colum[1])    
    song_contest = {"Year":years, "Country":countries }
    return song_contest 
print(read_song_contest("song_contest.txt"))

def read_scores(filename):
    marks_score ={}
    for line in open(filename):
        line =line.split(":")
        line



