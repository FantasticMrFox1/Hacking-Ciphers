# Caesar Cipher
# The second example of Hacking Secret Ciphers
# This only shifts the letters of a string, everything else stays.
# Not great for encrypting numbers / non-letters.
# Raymond Ho

def main():
    message = raw_input("Enter your message: ")
    mode = raw_input("E for Encrypt, D for Decrypt: ")
    key = int(raw_input("Enter your key: "))


    if mode == 'D' or mode == 'decrypt':
        key = -key

    print crypt(message, key)

def crypt(message, key):

    if key > 26 or key < 0: key = key % 26
    newString = ''

    for c in message:
        if c.isalpha():
            num = ord(c)
            num += key

            if c.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord ('A'):
                    num += 26
            elif c.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            newString += chr(num)
        else: newString += c

    return newString

if __name__ == '__main__':
    main()


