A bunch of fun encryption ciphers, hacked, in Python.
===

I'll be using Python 2.7 since it comes default on Mac

# Reverse Cipher
#### A super easy to understand algorithm. It basically reverses a given input string. To decipher/hack it, simply enter the encrypted string again.
#####Files:
* reverse.py

# Caesar Shift Cipher
#### Another easy to understand algorithm. Every character is shifted by N. For example, if the key was 3, then A->D, B->E, and so on. Z->C, since it just wraps around the alphabets.
#####Files:
* caesar.py
* caesarAdvanced.py - An advanced version of Caesar shift, shifts all characters, not just letters.
* caesarTest.py - A program to test caesar.py, runs it against a bunch of strings/key to ensure that it's working properly
* caesarHack.py - Hacks caesar.py, brute forces all 26 possible keys.


