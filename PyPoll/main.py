import os
import csv

election_data_csv = os.path.join('election_data.csv')

total_votes = 0
Charles_Stockham = []
Charles_percent = []
Diana_GeGette = []
Diana_percent = []
Raymon_Doane = []
Raymon_percent = []
total_net_votes = 0
Winner_total = 0

#opening the CSV file and formating layout of data in our csv
with open(election_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #counting total votes cast 
    header = next(csvreader)
    first_row = next(csvreader)
    total_votes += 1
    
    for row in csvreader
        total_votes +=1
        #counting votes for each candiate
        if row(2) == "Charles Casper Stockham"
            Charles_Stockham += 1
        elif row(2) == "Diana Degette"
            Diana_GeGette += 1
        elif row(2) == "Raymon Anthony Donane"
            Raymon_Doane += 1

#calculating the percent of each candiate
Charles_percent = round((Charles_Stockham / total_votes) * 100)
Diana_percent = round((Diana_GeGette / total_votes) * 100)
Raymon_percent = round((Raymon_Doane / total_votes) * 100)

print("Election Results")
print("------------------------")
print("Total Votes", total_votes)
print("------------------------")
print("Charles Casper Stockham:", charles_percent, "%", Charles_Stockham)
print("Diana Degette:", Diana_percent, "%", Diana_GeGette)
print("Raymon Anthony Donane:", Raymon_percent, "%", Raymon_Doane)
print("------------------------")
print("Winner:", Winner_total)
print("------------------------")
