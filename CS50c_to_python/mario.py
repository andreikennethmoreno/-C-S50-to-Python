#continues asks user for valid input
while True:
    height = int(input("Height: "))
    if ((height >= 1) and (height <= 8)):
        break
# prints dots and hashes
for i in range(height):
    for j in range(height - i - 1):
        print("  ", end="")
    for j in range(i + 1):
        print("# ", end="")
    print("")