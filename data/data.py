"""
https://corgis-edu.github.io/corgis/csv/astronauts/

Extras:
1) Use multiple aspects of a single data source in your analysis(DONE)
2) Use more than one data source and have your analysis compare,contrast, or correlate them(DONE)
"""

import csv

reader = csv.reader(open("astronauts.csv"))

#basic analysis: finding the average of the astronauts' birth years
sum = 0
num_of_astronauts = 0

for line in reader:
  if line[4] != "Profile.Birth Year":
    num_of_astronauts = num_of_astronauts + 1
    sum = sum + int(line[4])
print("The average of all the astronauts' birth years is", round(sum/num_of_astronauts), ".")

print("-------------------------------------------------------------------")

#extra 1: comparing "U.S.S.R/Russia" and "U.S." to see which average number of females to males
reader2 = csv.DictReader(open("astronauts.csv"))
data = [x for x in reader2]

#number of U.S. astronauts for each gender
US_astronauts = [x for x in data if x['Profile.Nationality'] == "U.S."]

US_astronauts_female = [x['Profile.Nationality'] for x in US_astronauts if x['Profile.Gender'] == "female"]
num_US_astronauts_female = len(US_astronauts_female)

US_astronauts_male = [x['Profile.Nationality'] for x in US_astronauts if x['Profile.Gender'] == "male"]
num_US_astronauts_male = len(US_astronauts_male)

#number of U.S.S.R/Russia astronauts for each gender
USSR_Russia_astronauts = [x for x in data if x['Profile.Nationality'] == "U.S.S.R/Russia"]

USSR_Russia_female = [x['Profile.Nationality'] for x in USSR_Russia_astronauts if x['Profile.Gender'] == "female"]
num_USSR_Russia_astronauts_female = len(USSR_Russia_female)

USSR_Russia_male = [x['Profile.Nationality'] for x in USSR_Russia_astronauts if x['Profile.Gender'] == "male"]
num_USSR_Russia_astronauts_male = len(USSR_Russia_male)


#comparing whether the U.S. or U.S.S.R had more astronauts
US_total_astronauts = num_US_astronauts_female + num_US_astronauts_male

USSR_Russia_total_astronauts = num_USSR_Russia_astronauts_female + num_USSR_Russia_astronauts_male

if US_total_astronauts > USSR_Russia_total_astronauts:
  print("The US had a greater number of astronauts than the USSR/Russia. \n")
else:
  print("The USSR/Russia had a greater number of astronauts than the US. \n")

print("US STATS:")
print("The number of female astronauts in the US is a total of", num_US_astronauts_female, ".")
print("The number of male astronauts in the US is a total of", num_US_astronauts_male, ".")
print("Total astronauts from the US:", US_total_astronauts, ". \n")

print("USSR/RUSSIA STATS:")
print("The number of female astronauts in the U.S.S.R/Russia is a total of", num_USSR_Russia_astronauts_female, ".")
print("The number of male astronauts in the U.S.S.R is a total of", num_USSR_Russia_astronauts_male, ".")
print("Total astronauts from the US:", USSR_Russia_total_astronauts, ".")

print("-------------------------------------------------------------------")

#EXTRA 2: comparing and constrasting the billionaire and astronaut data sources

reader3 = csv.reader(open("billionaires.csv"))

#finding the total number of billionaires
num_of_billionaires = 0

for line in reader3:
  if line[0] != "name":
    num_of_billionaires = num_of_billionaires + 1

print("There are", num_of_billionaires, "total billionaries compared to the total of", num_of_astronauts, "astronauts in the world.")
