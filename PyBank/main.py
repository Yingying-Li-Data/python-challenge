import os
import csv

csvpath= os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    rownumber = 0
    Total = 0
    Net = 0
    Previous = 0
    Change = 0
    Current_Change = 0
    Average = 0
    Max_Increase = 0
    Max_Decrease = 0

    for row in csvreader:
        
        rownumber = rownumber + 1
    
        if rownumber > 1:

            # The total number of months included in the dataset 
            Total = Total + 1

            # The net total amount of "Profit/Losses" over the entire period
            Net = int(Net) + int(row[1])
           
            if rownumber == 2:

                Previous = int(row[1])

            else:
                
                Current_Change = int(row[1]) - Previous
                Change = Change + Current_Change

                # The greatest increase in profits (date and amount) over the entire period
                
                if Current_Change > Max_Increase:
                    Max_Increase = Current_Change
                    Max_Increase_Month = row[0]

                # The greatest decrease in losses (date and amount) over the entire period

                if Current_Change < Max_Decrease:
                    Max_Decrease = Current_Change
                    Max_Decrease_Month = row[0]

                Previous = int(row[1])

# The average of the changes in "Profit/Losses" over the entire period
Average = round ( Change / (Total - 1), 2)

print("Financial Analysis")

print("----------------------------")

print(f'Total Months: {Total}')

print(f'Total: ${Net}')

print(f'Average  Change: ${Average}')

print(f'Greatest Increase in Profits: {Max_Increase_Month} (${Max_Increase})')

print(f'Greatest Decrease in Profits: {Max_Decrease_Month} (${Max_Decrease})')

# export a text file with the results

output_file = os.path.join("Results.text")

with open(output_file, "w") as outputfile:

    outputfile.write("Financial Analysis" + "\n")
    outputfile.write("----------------------------")
    outputfile.write(f'Total Months: {Total}' + "\n")
    outputfile.write(f'Total: ${Net}' + "\n")
    outputfile.write(f'Average  Change: ${Average}' + "\n")
    outputfile.write(f'Greatest Increase in Profits: {Max_Increase_Month} (${Max_Increase})' + "\n")
    outputfile.write(f'Greatest Decrease in Profits: {Max_Decrease_Month} (${Max_Decrease})' + "\n")