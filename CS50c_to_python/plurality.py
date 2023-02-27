class TestDat():
    def __init__(self, ):
        self.Dat1 = None
        self.Dat2 = None
   
    def __str__(self):
        return f"{self.Dat1} with {self.Dat2}"
   
TestArray = [] #empty array
size = 9       #number of loops

while True:
    for x in range(size):  # appending empty objects
        TestArray.append(TestDat())
        data = input(f"data {x}: ")
        TestArray[x].Dat1 = data
        TestArray[x].Dat2 = 0
        if (len(TestArray) < 2):
            print("At Least 2 candidates")
        elif (len(TestArray) > 9):
            print("Maximum of 9 candidates")
        elif(len(data) == 0):
            break
    if(len(data) == 0):
        break

numvotes =0
voters = int(input("number of voters: "))
for i in range(voters):
    name = input("Vote:")
    for j in range(len(TestArray)):
        if (name == TestArray[j].Dat1):
            TestArray[j].Dat2 += 1

maxv = max(TestArray, key=lambda x: x.Dat2)

print(f"the winner is {maxv} votes in total")
