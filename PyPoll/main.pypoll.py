import os
import csv

# Set path for file
csvPath = os.path.join('Resources', "election_data.csv")

# Open and read csv file
with open(csvPath, newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Create a path to export results to "Analysis" folder
    output_file = open("Analysis/Analysis.txt","w+")

    header = next(csvReader)
    total_votes = 0
    total_candidates = []
    candidates_list = []
    candidate_votes = {}
    votes_average = []
    winner = ''
    votes = 0
   
    # Your task is to create a Python script that analyzes the records to calculate each of the following:
    print("Election Results")
    print("---------------------------------")
    output_file.write("Election Results\n")
    output_file.write("---------------------------------\n")

    for row in csvReader:
    
        # The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes
        name = row[2] 
        if name not in candidates_list:
            candidates_list.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] += 1

    print(f'Total Votes: {total_votes}')
    print("---------------------------------")
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write("---------------------------------\n")
    
     # The total number of votes each candidate won
    for candidate in candidate_votes:

        # The percentage of votes each candidate won
        votes_average = ((candidate_votes[candidate]* 100) / total_votes)
        print(f'{candidate}: {votes_average:,.3f}% ({str(candidate_votes[candidate])})')
        output_file.write(f'{candidate}: {votes_average:,.3f}% ({str(candidate_votes[candidate])})\n')
        
        # The winner of the election based on popular vote.
        if votes < candidate_votes.get(candidate):
            winner = candidate
            votes = candidate_votes.get(candidate)
        
    print("---------------------------------")
    print(f'Winner: {winner}')
    output_file.write("---------------------------------\n")
    output_file.write(f'Winner: {winner}\n')