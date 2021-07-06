import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    rownumber = 0
    Total_Vote = 0
    Candidates = []

    for row in csvreader:

        rownumber = rownumber + 1

        if rownumber > 1:

            # The total number of votes cast
            Total_Vote = Total_Vote + 1

            if row[2] not in Candidates:
                
                Candidates.append(row[2])

print("Election Results")
print("-------------------------")
print(f'Total Votes: {Total_Vote}')
print("-------------------------")

Max_Vote = 0

# A complete list of candidates who received votes
for candidate in Candidates:

    Votes = 0

    with open(csvpath) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:

            if row[2] == candidate:

                # The total number of votes each candidate won
                Votes = Votes + 1

    # The percentage of votes each candidate won
    Votes_Percent = "{:.3%}".format(Votes/Total_Vote)

    print(f'{candidate}: {Votes_Percent} ({Votes})')        

    if Votes > Max_Vote:

        Max_Vote = Votes
        Winner = candidate

# The winner of the election based on popular vote.

print("-------------------------")
print(f'Winner: {Winner}')
print("-------------------------")

# export a text file with the results

output_file = os.path.join("Results.text")

Max_Vote = 0

with open(output_file, "w") as outputfile:

    outputfile.write("Election Results" + "\n")
    outputfile.write("-------------------------" + "\n")
    outputfile.write(f'Total Votes: {Total_Vote}' + "\n")
    outputfile.write("-------------------------" + "\n")

    for candidate in Candidates:

        Votes = 0

        with open(csvpath) as csvfile:

            csvreader = csv.reader(csvfile, delimiter=',')

            for row in csvreader:

                if row[2] == candidate:

                    # The total number of votes each candidate won
                    Votes = Votes + 1

        # The percentage of votes each candidate won
        Votes_Percent = "{:.3%}".format(Votes/Total_Vote)

        outputfile.write(f'{candidate}: {Votes_Percent} ({Votes})' + "\n")        

        if Votes > Max_Vote:

            Max_Vote = Votes
            Winner = candidate

    outputfile.write("-------------------------" + "\n")
    outputfile.write(f'Winner: {Winner}' + "\n")
    outputfile.write("-------------------------" + "\n")
