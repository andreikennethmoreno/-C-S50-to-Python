class TestDat:
    
    def __init__(self, city, temp):
        self.item = city
        self.price = temp

if __name__ == '__main__':
 
    Menu = [TestDat("BURGER",9.5),
             TestDat("VEGAN BURGER",11.0),
             TestDat("Chicago",85),
             TestDat("Denver",90),
             TestDat("Las Vegas",105),
             TestDat("Los Angeles",82),
             TestDat("Miami",97),
             TestDat("New York",85),
             TestDat("Pheonix",107),
             TestDat("San Francisco",66),]
 
print("Welcome to Beach Burger Shack!")
print("Choose from the following menu to order. Press enter when done.")
#prints all the items in the menu array
for i in range(len(Menu)):
    print(Menu[i].item ,":" , "$", Menu[i].price)

total = 0
while True :
    #asks the user for the order
    item = input("Enter a food item: ").upper()
    if(len(item) == 0):
        break
    #compare the order of teh user to the array
    for i in range(len(Menu)):
        if (item == Menu[i].item):
            total += Menu[i].price
    #if no order stop loop


#compares input through the array
print(f"\nyour total is {total}")

