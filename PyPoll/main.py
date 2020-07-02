import os
import csv

# Set path for file
csvPath = os.path.join('Resources', "election_data.csv")

# Open and read csv file
with open(csvPath, newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Create a path to export results to "Analysis" folder
    # output_file = open("Analysis/Analysis.txt","w+")

    header = next(csvReader)
    # first_row = next(csvReader)
    total_votes = 0
    total_candidates = []
    candidates_list = []
    candidate_dict = {}
   
    # Your task is to create a Python script that analyzes the records to calculate each of the following:
    # print("Election Results")
    # print("---------------------------------")

    for row in csvReader:
    
        # The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes
        name = row[2] 
        if name not in candidates_list:
            candidates_list.append(name)
            candidate_dict[name] = 0
        candidate_dict[name] = candidate_dict[name] + 1

        # The percentage of votes each candidate won

        # The total number of votes each candidate won

        # The winner of the election based on popular vote.

    print(f'Total Votes: {total_votes}')
    print("---------------------------------")
    for candidate in candidates_list:
        print(candidate + " has " + str(candidate_dict[candidate]) + " total votes")