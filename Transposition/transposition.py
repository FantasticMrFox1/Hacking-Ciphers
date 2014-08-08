# Transposition Cipher
# Create N boxes to store letters in.
# Write in rows, read in columns.
# This cipher is more secure than Ceasar shift.
# USAGE: python transposition.py [optional file]
# Raymond Ho

import math, sys

def main():

    string = ''

    # User manually enters string
    if len(sys.argv) == 1:
        string = raw_input("Enter your string: ")

    # User inputs a file.
    else:
        with open(sys.argv[1], 'r') as f:
            string = f.read()

    key = int(raw_input("Enter your key: "))
    mode = raw_input("E for encrypt, D for Decrypt: ")

    print("Processing data...\n")

    result = ''

    if mode == 'E':
        result = encrypt(string, key)
    elif mode == 'D':
        result = decrypt(string, key)

    # If there were arguments, save to file, rather than printing.
    if len(sys.argv) > 1:
        outputFile = mode + '.' + sys.argv[1]
        with open(outputFile, 'w') as f:
            f.write(result)
        print '"%s": %s characters written.' % (outputFile, len(result))
    else:
        # In case there are spaces at the end of the cipher
        print (result + '|')

def encrypt(string, key):

    # Each string in cipher represents a column in grid.
    cipher = [''] * key

    # Loop through each column
    for col in range(key):
        pointer = col

        # Go through the entire string, skipping 'key' characters.
        while pointer < len(string):
            # Append to array
            cipher[col] += string[pointer]
            pointer += key

    return ''.join(cipher)

def decrypt(string, key):

    # Length of message / key, then round up.
    columns = int(math.ceil((len(string) / float(key))))
    rows = key
    blank = (columns * rows) - len(string) # This is the shaded boxes
    cipher = [''] * columns

    col = row = 0

    # Iterate the string, character by character.
    for char in string:
        cipher[col] += char
        col += 1

        # If there are no more columns OR arrived at shaded box,
        # Go back to first column, and next row.
        if (col == columns) or (col == columns - 1 and row >= rows - blank):
            col = 0
            row += 1

    return ''.join(cipher)

if __name__ == '__main__':
    main()

