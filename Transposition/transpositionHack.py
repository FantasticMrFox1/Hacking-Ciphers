# Transposition Cipher Hacker
# A program that brute forces as many keys as neccessary to crack
# an encrypted transposition cipher. It takes a string and attempts
# to break it apart to match with words in the dictionary

# Raymond Ho

import sys
import detectEnglish, transposition

def main():

    message = ''

    # No arguments
    if len(sys.argv) == 1:
        message = raw_input("Enter message to hack: ")
    # 1 argument
    else:
        with open(sys.argv[1], 'r') as f:
            message = f.read()
    hackedMessage = hackTransposition(message)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        if len(hackedMessage) > 1000:
            newFile = 'hacked.' + sys.argv[1]
            with open(newFile, 'w') as f:
                f.write(hackedMessage)
            print('Hack successful! File saved to: %s' % (newFile))
        else:
            print(hackedMessage)

def hackTransposition(message):
    print('Hacking...')

    # Brute force time!
    for key in range(1, len(message)):
        print('Trying key #%s..' % (key))

        decryptedText = transposition.decrypt(message, key)

        if detectEnglish.isEnglish(decryptedText):
            print('\nPossible encryption hack:')
            print('Key %s: "%s"' % (key, decryptedText[:50]))
            response = raw_input('Enter D for done, or ENTER to continue: ')
            if response == 'D':
                return decryptedText
    # If loop finishes
    return None

if __name__ == '__main__':
    main()

