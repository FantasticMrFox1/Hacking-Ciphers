# Vigenere Cipher Testing
# This program is used to test "vigenere.py"
# Tests random strings and keys to ensure algorithm is correct.
# Raymond Ho
# Created on August 18th, 2014.

import random, sys, string, vigenere

def main():

    for i in range(100): # Amount of tests

        string = random_string()
        key = random_string()
        print ('Test #%s: String: "%s.."\nKey: %s..' % (i + 1, string[:50], key[:50]))

        encrypted = vigenere.translate(string, key, 0)
        decrypted = vigenere.translate(encrypted, key, 1)

        # If decrypted message is not the same as original
        if string != decrypted:
            print('ERROR: Decrypted: "%s"  Key: %s' % (decrypted, key))
            sys.exit()

    print('Vigenere cipher test passed.')

# Algorithm found on stackoverflow
def random_string(size = 5000, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    main()


