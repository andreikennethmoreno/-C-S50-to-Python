#asks user for key
skey = input("Key: ")
#checks whther the input is less than 1 or a digit
if (((len(skey) != 2)) and (not skey.isdigit())):
    print("Usage key: int\n")
#converts string digit to int
ikey = int(skey)
#asks user for plain text
text = input("plaintext: ")
cipher = print("ciphertext: ", end = '')
for i in range(len(text)):
    if ((text[i]).isupper()):
        #adds the num val of the key to the ascii equivalent of the text char
        print(chr((ord(text[i]) - 65 + ikey ) %26 + 65 ), end = '')
    elif ((text[i]).islower()):
        #adds the num val of the key to the ascii equivalent of the text char
        print(chr((ord(text[i]) - 97 + ikey ) %26 + 97 ),end = '')
    else:
        print(text[i], end = '')