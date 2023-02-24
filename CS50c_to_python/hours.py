from array import*
#empty array that stores int
hours = array('i', [])
#defines the size of the array
weeks = int(input("Number of weeks taking CS50: "))
#inserts data into the array
for i in range(weeks):
    x = int(input(f"Week {i} HW Hours: "))
    hours.append(x)
#a choice whether to get avg or total
while True:
    output = input("Enter T for total hours, A for average hours per week: ").upper()
    if (output == 'T' or output == 'A'):
        break
sum = 0
#gets the avg
if(output == 'A'):
    for i in range(weeks):
        sum = x + x
#gets the total
    sum = sum / float(weeks)
else:
    for i in range(weeks):
        sum = x + x
#prints the total
print(f"{sum} hours")