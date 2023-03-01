#asks user for teh candidates
preference = {}
#max candidates
maxcandi = 9

candidates = list(map(str, input("candidates: ").split()))

for x in range(len(candidates)):
    preference[candidates[x]] = 0

#conditions for the required num of candidates
if (len(candidates) < 2):
    print("At Least 2 candidates")
elif (len(candidates) > maxcandi):
    print("Maximum of 9 candidates")
   
#asks user for num of voters
numofvoters = int(input("number of voters: "))

#asks user for the ranking deoending on the num of candidates
for y in range(numofvoters):
    for z in range(len(candidates)):
        ranking = input(f"Rank {z + 1}: ")

        if preference.get(ranking)!=None:
            preference[ranking] += 1 + z
            print("it matches")
            
            print(preference)
    print("\n")

#print the winner
minvalue = min(preference.values())
minkeys = [k for k in preference if preference[k] == minvalue]

if len(minkeys) == 1:
    print(f"the winner of the electiona is {minkeys}")
else: 
    print(f"the winners of the electiona are {minkeys}")
