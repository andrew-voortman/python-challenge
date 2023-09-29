# import modules
import os
import csv

# I created an empty list to append the csv file data to.
# I opened the .csv file and read it into my python file.
csvpath = os.path.join('Resources', 'election_data.csv')

data_list = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        data_list.append(row)



print('Election Results')
print('-------------------------')

# I created a variable for the total votes cast and set it 
# equal to the length of the data_list.
all_votes = int(len(data_list))
print(f'Total Votes: {all_votes}')
print('-------------------------')

# I created an empty list for the cadidates and iterated over the 
# data_list to find all candidates in column 3 and append them to 
# the empty list.
candidates = []

for vote in data_list:
    candidate = vote[2]
    if candidate not in candidates:
        candidates.append(candidate)

# I created a counter for each cadidate found above and iterated over
# the data list using column 3 and adding 1 to the value of the candidate
# every time their name appears.
Stockham = 0
DeGette = 0
Doane = 0

for vote in data_list:
    candidate = vote[2]

    if candidate == "Charles Casper Stockham":
        Stockham += 1
    elif candidate == "Diana DeGette":
        DeGette += 1
    elif candidate == "Raymon Anthony Doane":
        Doane += 1

# I calculated the percentage of the total vote each candidate received 
# (to the third decimal point) by using the counter variables created above 
# for each candidate and all_votes, and put them into print statements for 
# each candidate. I also included code in the print statement to present the
# total vote count per candidate by casting the variables for each as strings.
print("Votes for Charles Casper Stockham: " + str(round(Stockham / all_votes * 100,3)) + " % (" + str(Stockham) + ')')
print("Votes for Diana DeGette: " + str(round(DeGette / all_votes * 100,3)) + " % (" + str(DeGette) + ')')
print("Votes for Raymon Anthony Doane: " + str(round(Doane / all_votes * 100,3)) + " % (" + str(Doane) + ')')

# I created a nested list of outcomes and used it in the variable I created
# named 'maximum' which I then iterated over (column 2) to find the maximum
# number and print the corresponding name (column 1).
outcomes = [["Charles Casper Stockham", Stockham],
            ["Diana DeGette", DeGette],
            ["Raymon Anthony Doane", Doane]]

maximum = outcomes[0]

for item in outcomes:
    if item[1] > maximum[1]:
        maximum = item
print('-------------------------')
print('Winner: ' + maximum[0])
print('-------------------------')

# Finally, open the analysis.txt file and output all of the print statements.
# Do this by creating a list variable which includes the contents of each print 
# statement. Then use that to 'write' each statement to the .txt file using a for loop.
# close the .txt file.
output = ['Election Results',
          '-------------------------',
          f'Total Votes: {all_votes}',
          '-------------------------',
          "Votes for Charles Casper Stockham: " + str(round(Stockham / all_votes * 100,3)) + " % (" + str(Stockham) + ')',
          "Votes for Diana DeGette: " + str(round(DeGette / all_votes * 100,3)) + " % (" + str(DeGette) + ')',
          "Votes for Raymon Anthony Doane: " + str(round(Doane / all_votes * 100,3)) + " % (" + str(Doane) + ')',
          '-------------------------',
          'Winner: ' + maximum[0],
          '-------------------------']

with open('analysis/analysis.txt', 'w') as f:
    for line in output:
        f.writelines(str(line))
        f.write('\n')

f.close()