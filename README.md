A bunch of fun encryption ciphers, hacked, in Python.
===

I'll be using Python 2.7 since it comes default on Mac

# Reverse Cipher
#### A super easy to understand algorithm. It basically reverses a given input string. To decipher/hack it, simply enter the encrypted string again.
##### Files:
* reverse.py - The main program: enter a string, it'll reverse it for you.

# Caesar Shift Cipher
#### Another easy to understand algorithm. Every character is shifted by a key. For example, if the key was 3, then A->D, B->E, and so on. Z->C, since it just wraps around the alphabets.
##### Files:
* caesar.py
* caesarAdvanced.py - An advanced version of Caesar shift, shifts all characters, not just letters.
* caesarTest.py - A program to test caesar.py, runs it against a bunch of strings/key to ensure that it's working properly
* caesarHack.py - Hacks caesar.py, brute forces all 26 possible keys.

# Transposition Cipher
#### A little tougher to crack compared to Caesar Shift. Given a key N, this algorithm creates N columns of arrays. For each character in a given string, it will fill up the table from left to right, but READ it top to bottom. For example: "Hello Raymond" with key 5 will be read as "H oeRnladlyom". To decipher this, you do some fancy math to find the correct number of columns, and do as you would to encrypt. 
#### Hacking this is harder, since they number of keys is proportional to the length of the string, a long string can have a bunch of possibie keys. So, we must split the string into words, and brute force each word against the key, and compare the results to words in the English dictionary. If there are enough matches of words, we can say with enough certainty that we have the correct key.
##### Files:
* transposition.py - The main program, used to en/decrypt strings with a given key.
* transpositionTest.py - Ensures that our program's algorithm is running correctly by testing 1000 random strings/keys.
* transpositionHack.py - Works with detectEnglish.py to crack transposition.py's encryption.
* detectEnglish.py - Given a string, determines how many of "words" can be found in dictionary.txt
* dictionary.txt - a list of English words

