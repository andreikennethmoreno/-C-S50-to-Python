from array import*
#sorted alphabetical score points
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#askes players for the word
word1 = input("Player 1: ")
word2 = input("Player 2: ")
#a fucniton that computes teh score of a word
def compute_score(word):
    score = 0
    #a loop that depends on the length of the word
    for i in range(len(word)):
        #checks if upper or not
        if ((word[i]).isupper()):
            #turns the char into its ASCII equivalent 
            #subtract it to 65 bcs 'A' is on position 65
            #after subtracting it you get the exact index of the points
            score += POINTS[ord(word[i]) - 65]
        #checks if lower
        elif ((word[i]).islower()):
            #turns the char into its ASCII equivalent 
            #subtract it to 97 bcs 'a' is on position 97
            #after subtracting it you get the exact index of the points
            score += POINTS[ord(word[i]) - 97]
    return score
#computes the score of the words
score1 = compute_score(word1)
score2 = compute_score(word2)
#compares the scores to see who's the winnner
if score1 > score2:
    print(f"{score1} > {score2} player 1 wins!")
elif score2 > score1:
    print(f"{score2} > {score1} player 2 wins!")
else:
    print("its a tie")
