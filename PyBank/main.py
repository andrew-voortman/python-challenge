# import modules
import os
import csv

# I created an empty list to append the csv file data to.
month_list = []

# I opened the .csv file and read it into my python file.
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        month_list.append(row)

# I entered the first print statements here after reading in the csv data to
# populate the empty list variable above.

print('Financial Analysis')
print('----------------------------')

# I created a variable for the length 'len' of months in the dataset and 
# print the variable to get our first bit of data output.
total_months = str(len(month_list))
print(f'Total Months: {total_months}')

# I created a counter for the total profit that I added '+=' to by iterating
# through the dataset and adding the values in the second column.
# print the variable to get total profit/loss across all months.
profit_total = 0

for month in month_list:
    profit_total += int(month[1])

print(f"Total: ${profit_total}")

# I created another empty list for the profit changes from month to month which I then 
# calculated by iterating through using a for loop and range (setting range equal to the length of the 
# rows-1 so we don't get an indexing error due to a missing month at the end of the data set). 
# I then created two variables to gather the number from column 2 from each month and
# each month+1 so I could use those variables to subtract and get the change per month
# and append those values to the empty list 'profit_changes'. I then used the (now
# polulated) lsit to calculate the average sum of all profit changes and the length
# of the profit changes.
# Finally, I created the print statment.
profit_changes = []

for month in range(0, len(month_list)-1):
    profit1 = int(month_list[month][1])
    profit2 = int(month_list[month+1][1])

    change = profit2 - profit1

    profit_changes.append(change)

length = len(profit_changes)
total = sum(profit_changes)

average_change = total / length
print("Average Change: $" + str(round(average_change,2)))

# I did the same thing here by creating another empty list that
# I then populated with the [month of change][change] since I knew the
# print statement needed to show the month and value for max and min.
changes_per_month = []

for month in range(0, len(month_list)-1):
    profit1 = int(month_list[month][1])
    profit2 = int(month_list[month+1][1])

    change = profit2 - profit1
    
    changes_per_month.append([month_list[month+1][0], change])

# I created variables for maximum and minimum using the iterable changes_per_month
# list we created above starting at the first row. Then iterate through them with
# the logic being that you have the code ask: is the item in column 2 bigger than 
# what is currently set to maximum? If so, set that to maximum. Set the opposite to 
# be true for minimum. That way you will end up with the max and min value changes.
# print.
maximum = changes_per_month[0]
minimum = changes_per_month[0]

for item in changes_per_month:
    if item[1] > maximum[1]:
        maximum = item
    
    elif item[1] < minimum[1]:
        minimum = item

print('Greatest Increase in Profits: ' + str(maximum))
print('Greatest Decrease in Profits: ' + str(minimum))

# Finally, open the analysis.txt file and output all of the print statements.
# Do this by creating a list variable which includes the contents of each print 
# statement. Then use that to 'write' each statement to the .txt file using a for loop.
# close the .txt file.
output = 'Financial Analysis','----------------------------',f'Total Months: {total_months}',f"Total: ${profit_total}","Average Change: $" + str(round(average_change,2)),'Greatest Increase in Profits: ' + str(maximum),'Greatest Decrease in Profits: ' + str(minimum)

with open('analysis/analysis.txt', 'w') as f:
    for line in output:
        f.writelines(str(line))
        f.write('\n')

f.close()
