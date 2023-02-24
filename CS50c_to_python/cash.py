#prompts the user to input a positive int
while True:
    cents = int(input("Change owed: "))
    if (cents > 0):
        break
    
def calculate_quarters(cents):
    quarters = 0
    while (cents >= 25):
        cents = cents - 25
        quarters += 1
    return quarters

def calculate_dimes(cents):
    dimes = 0
    while (cents >= 10):
        cents = cents - 10
        dimes += 1
    return dimes

def calculate_nickels(cents):
    nickels = 0
    while (cents >= 5):
        cents = cents - 5
        nickels += 1
    return nickels

def calculate_pennies(cents):
    pennies = 0
    while (cents >= 1):
        cents = cents - 1
        pennies += 1
    return pennies


quarters = calculate_quarters(cents)
cents = cents - quarters * 25

dimes = calculate_dimes(cents)
cents = cents - dimes * 10

nickels = calculate_nickels(cents)
cents = cents - nickels * 5

pennies = calculate_pennies(cents)
cents = cents - pennies * 1

coins = quarters + dimes + nickels + pennies

print(coins)