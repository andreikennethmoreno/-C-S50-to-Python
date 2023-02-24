#prompts and only outputs lower case words
word = input("word: ").lower()
#replaces  a e i o with int
no_vowels = word.replace('a', '6').replace('e', '3').replace('i', '1').replace('o', '0')
print(no_vowels)