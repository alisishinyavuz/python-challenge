import os
import csv

csvpath = os.path.join("Resources/election_data.csv")

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
    next(csvreader)

    for row in csvreader:
        #Add the vote in every row
        count += 1

        #If the candidate is not in the candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
            num_votes.append(1)
            index= candidates.index(row[2])

        #If the candidate is in the candidates list
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




txt_path = os.path.join('election_results.txt')

with open(txt_path, 'w') as txtfile:

    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {str(count)}
-------------------------\n''')

    print(f'''\n Election Results
-------------------------
Total Votes: {str(count)}
-------------------------''')

    for i in range(len(candidates)):
        txtfile.write(f'{candidates[i]}:{str(percentage_votes[i])} ({str(num_votes[i])})\n')
        print(f'''{candidates[i]}:{str(percentage_votes[i])} ({str(num_votes[i])})''')

    
    txtfile.write(f'''-------------------------
Winner: {winning_candidate}
-------------------------''')

    print(f'''-------------------------
Winner: {winning_candidate}
-------------------------''')





