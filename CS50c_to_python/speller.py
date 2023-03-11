#import pyenchant on PyPi
import enchant
#for .txt files
with open('textfile.txt') as words:
	   lines = words.readlines()

mystr =' '.join(map(str,lines))

new_str = ''
for char in mystr:
    #all not isalnum except for space
   if char not in ('!', '"',"#","$",'%','^','&','*','(',')','+',',','.','-','/',':',';','<','=','>','?','@','[',']','{','}','_','~','\n'):
        new_str += char
print(new_str)

#for user input
# user_input = input("sentence: ").lower()

# new_str = ''
# for char in user_input:
#     #all not isalnum except for space
#     if char not in ('!', '"',"#","$",'%','^','&','*','(',')','+',',','.','-','/',':',';','<','=','>','?','@','[',']','{','}','_','~'):
#         new_str += char

word_list = new_str.split(" ")
words_in_dict = 0
words_misspelled = 0

print(word_list)

print("MISSPELLED WORDS: ")

d = enchant.Dict("en_US")

for i in range(len(word_list)):
    valid = d.check(word_list[i])
    if valid == True:
        words_in_dict += 1
    else:
        words_misspelled += 1
        print(word_list[i])

print(f"WORDS IN DICTIONARY: {words_in_dict}")
print(f"WORDS MISSPELLED : {words_misspelled}")
print(f"WORDS IN TEXT: {len(word_list)}")

