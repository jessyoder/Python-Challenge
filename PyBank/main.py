import os
import csv

# Set path for file
csvPath = os.path.join('Resources', "budget_data.csv")

# Open and read csv file
with open(csvPath, newline="") as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')

  # Create a path to export results to "Analysis" folder
  output_file = open("Analysis/Analysis.txt","w+")

  header = next(csvReader)
  first_row = next(csvReader)
  month_count = 0
  total_amt = 0
  prev_net = int(first_row[1])
  net_change_list = []
  month_list = []

  maximum = 0
  minimum = prev_net
   
  # Your task is to create a Python script that analyzes the records to calculate each of the following:
  output_file.write("Financial Analysis\n")
  output_file.write("---------------------------------\n")

  for row in csvReader:

    # The total number of months included in the dataset
    month_count += 1

    # The net total amount of "Profit/Losses" over the entire period
    total_amt += int(row[1])

    # The average of the changes in "Profit/Losses" over the entire period
    net_change = int(row[1]) - prev_net
    prev_net = int(row[1])
    net_change_list += [net_change]
    #month_list.append(row[0])

    # print(net_change_list)
    average_change = sum(net_change_list) / month_count
    
    # The greatest increase in profits (date and amount) over the entire period
    # during iteration, get a month if we capture the newest maximum or minimum
    # If so, once the loop is done, we will have months for maximum and minimum
    if net_change > maximum:
      maximum_month = row[0]
      maximum = net_change
    # The greatest decrease in losses (date and amount) over the entire period
    if net_change < minimum:
      minimum_month = row[0]
      minimum = net_change
        
  output_file.write(f'Total Months: {month_count} \n')  
  output_file.write(f'Total: ${total_amt}\n')
  output_file.write(f'Average Change: ${round(average_change,2)}\n')
  output_file.write(f'Greatest Increase in Profits: {maximum_month} ({max(net_change_list)})\n')
  output_file.write(f'Greatest Decrease in Profits: {minimum_month} ({min(net_change_list)})\n')  