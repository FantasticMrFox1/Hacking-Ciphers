# Transposition Cipher Testing
# This program is used to test "transposition.py"
# Tests random strings and keys to ensure algorithm is correct.
# Raymond Ho
# Created on August 6th, 2014.

import random, sys, string, transposition

def main():

    for i in range(10): # Amount of tests

        string = random_string()
        key = random.randint(1, 50)
        print ('Test #%s: String: "%s.." Key: %s' % (i + 1, string[:50], key))

        encrypted = transposition.encrypt(string, key)
        decrypted = transposition.decrypt(encrypted, key)

        # If decrypted message is not the same as original
        if string != decrypted:
            print('ERROR: Decrypted: "%s"  Key: %s' % (decrypted, key))
            sys.exit()

    print('Transposition cipher test passed.')

# Algorithm found on stackoverflow
def random_string(size = 5000, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    main()


