import os
import csv

# Set path for file, open and read csv file
csvPath = os.path.join('Resources', "budget_data.csv")

month_count = 0
total_amt = 0
average = 0

with open(csvPath, newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Check to see if csvReader Row 1 will print.
    # for row in csvReader:
    #     print(row[0])

    # Skip Header Row
    Header = next(csvReader)
    #print(Header)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
    print("Financial Analysis")
    print("---------------------------------")

    for row in csvReader:

      # The total number of months included in the dataset
      month_count += 1

      # The net total amount of "Profit/Losses" over the entire period
      total_amt += int(row[1])

      # The average of the changes in "Profit/Losses" over the entire period
      average = total_amt / month_count
      # The greatest increase in profits (date and amount) over the entire period

      # The greatest decrease in losses (date and amount) over the entire period
        
    print(f'Total Months: {month_count}')  
    print(f'Total: ${total_amt}')
    print(f'{average}')
       
  
  