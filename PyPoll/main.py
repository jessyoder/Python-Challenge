import os
import csv

# Set path for file
csvPath = os.path.join('Resources', "election_data.csv")

votes_count = 0

# Open and read csv file
with open(csvPath, newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Skip Header Row
    # Header = next(csvReader)
    # print(Header)

    # Your task is to create a Python script that analyzes the votes and calculates each of the following:
    print("Election Analysis")
    print("---------------------------------")

    for row in csvReader:

        # The total number of votes cast
        votes_count += 1

        # A complete list of candidates who received votes

        # The percentage of votes each candidate won

        # The total number of votes each candidate won

        # The winner of the election based on popular vote.
