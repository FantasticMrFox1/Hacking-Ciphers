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
#### Hacking this is harder, since they number of keys is proportional to the length of the string, a long string can have a bunch of possible keys. So, we must split the string into words, and brute force each word against the key, and compare the results to words in the English dictionary. If there are enough matches of words, we can say with enough certainty that we have the correct key.
##### Files:
* transposition.py - The main program, used to en/decrypt strings with a given key.
* transpositionTest.py - Ensures that our program's algorithm is running correctly by testing 1000 random strings/keys.
* transpositionHack.py - Works with detectEnglish.py to crack transposition.py's encryption.
* detectEnglish.py - Given a string, determines how many of "words" can be found in dictionary.txt
* dictionary.txt - a list of English words

# Substitution Cipher
#### A more advanced version of Caesar Cipher. Instead of shifting letters of the Alphabets by a key, letters are directly replaced by other letters of the alphabet, resulting in a 26 unique characters key. This gives a possibility of 26!(factorial) combinations! So instead of brute forcing each possible key, we want to map each word to its cipher pattern, so we can compare them to those similar in the dictionary. A word's pattern is determined by the amount of unique letters it has. Example: 'Hello' = '0.1.2.2.3' and 'Raymond' = '0.1.2.3.4.5.6.7' and 'Happy' = '0.1.2.2.3'. See how 'Hello' and 'Happy' maps to the same pattern? That's how we can determine possible substitutions.
##### Files:
* substitution.py - The main program: en/decrypts a string/file with a 26 character key.
* substitutionTest.py - Tests our main program by generating random strings/keys to ensure algorithm is correct.
* makeWordPatterns.py - A program to create a python file.
* wordPatterns.py - Created by makeWordPatterns.py. Contains a single map of all the words in the dictionary, and their corresponding cipher pattern.
* subHack.py - Copied algorithms directly from Hacking Ciphers book. This program is used to find intersection of words. The more words in a string the better, to eliminate bad substitutions. Prints the potential key map, and (possible) deciphered text.
* dictionary.txt - Needed again by makeWordPatterns.py
* textfile.txt/enc.textfile.txt/hacked.enc.textfile.txt - See how well our program did by comparing hacked.enc.textfile.txt and the original textfile.txt

# Vigenere Cipher
#### Another variation of the Caesar Cipher. The key consists of multiple shifts. The key is often a word, where each letter of the word is a subkey. A = 0, Z = 25, and everything in between.
##### Files:
* vigenere.py - The main program: en/decrypts a string/file with a key of user's choice.
* vigenereTest.py - Tests the main program to ensure algorithms is working correctly.

