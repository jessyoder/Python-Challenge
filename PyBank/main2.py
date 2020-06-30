import os
import csv

# Set path for file, open and read csv file
csvPath = os.path.join('Resources', "budget_data.csv")

month_count = 0
total_amt = 0
average = 0

with open(csvPath, newline="") as csvFile:

    difference = [] 

    csvReader = csv.reader(csvFile, delimiter=',')

    # Check to see if csvReader Row 1 will print.

    

    # Skip Header Row
    Header = next(csvReader)
    #print(Header)

    # print("Financial Analysis")
    # print("---------------------------------")

    for row in csvReader:
        #print(row[1])
        difference = str((csvReader[1] + 1) - csvReader[1])

    print(difference)

    #for row in csvReader: 