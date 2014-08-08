# Caesar Shift Hacker
# This program brute forces all 26 possible keys.
# Raymond Ho

string = raw_input("Enter the string to decipher: ")

for key in range(26):
    translated = ''
    for letter in string:
        if letter.isalpha():
            num = ord(letter)
            num -= key

            if letter.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letter.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else: translated += letter
    print ('Key %i: %s' % (key, translated))

