#start size has to be greater then 9
while True:
    start = int(input("Start size: "))
    if (start >= 9):
        break
#end size input should be greater than end
while True:
    end = int(input("End size: "))
    if (start <= end):
        break
#a loop to count the number of years
count = 0
while (start < end):
    start += (start / 3) - ( start / 4)
    count += 1
print(f"Years: {count - 1}")