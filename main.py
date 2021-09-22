import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Collect all the number of votes for each candidate
num_votes= []
#Collect all the candidate names in a list
candidates =[]
#Collect the percentage of total votes for each candidate
percentage_votes =[]
#Count the total number of votes
count = 0


with open (csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter = ",")
    #Skip the header row
    csv_header = next(csvreader)

    for row in csvreader:
        #Add the vote in every row
        count += 1

        #If the candidate is not in the candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
            num_votes.append(1)
            index= candidates.index(row[2])

        
        else:
             index =candidates.index(row[2])
             num_votes[index]+=1



    for votes in num_votes:
        percentage = (votes/count)*100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentage_votes.append(percentage)


        winner = max(num_votes)
        index = num_votes.index(winner)
        winning_candidate = candidates[index]




print(f'Election Results')
print("-------------------------------")
print(f'Total votes: {str(count)}')
print("-------------------------------")

for i in range(len(candidates)):
    print(f'{candidates[i]}:{str(percentage_votes[i])} ({str(num_votes[i])})')
    
print("-----------------------------")
print(f'Winner:{winning_candidate}')
print("------------------------------")



