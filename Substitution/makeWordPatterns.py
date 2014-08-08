# Creates the wordPatterns.py file
# For each word in 'dictionary.txt', find its pattern
# Example: doggy = 0.1.2.2.3
#          water = 0.1.2.3.4
# Raymond Ho
# August 7th, 2014

# For pretty printing: useful for printing dicts and lists
import pprint

def getWordPattern(word):
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)

def main():

    allPatterns = {}

    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # Create and write to wordPatterns.py
    # Hardcodes allPatterns in.
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()

if __name__ == '__main__':
    main()

