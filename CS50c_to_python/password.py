lower = False
upper = False
digit = False
symbol = False
valid = False

while valid != True:    
    passw = input('enter your password: ')

    for c in passw:
        if c.islower():
            lower = True
        if c.isupper():
            upper = True
        if c.isdigit():
            digit = True
        if not c.isalnum():
            symbol = True

    if lower == True and upper == True and digit == True and symbol == True:
        print("password valid")
        valid = True
    else:
        print("need 1 upper, lower , symbol and digit")
        valid = False


        






