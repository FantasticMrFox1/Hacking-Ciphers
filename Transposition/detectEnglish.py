# Detect English

# USAGE:
#   import detectEnglish
#   detectEnglish.isEnglish(string)
# returns True or False

# 'dictionary.txt' file must be in directory
# 'dictionary.txt' contains list of words, one per line.

# This program checks if a string is in dictionary.
# Raymond Ho

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    words = {}
    for word in dictionaryFile.read().split('\n'):
        words[word] = None
    dictionaryFile.close()
    return words

ENGLISH_WORDS = loadDictionary()

# Does string manipulation to find percentage of words in dictionary
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

# Keeps only letters and spaces/tabs/newlines
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

# The main function to be called.
# Returns true if percentage of a message is English >= wordPercentage
# Example: This function returns true if message given has 20% English
def isEnglish(message, wordPercentage = 20):
    return getEnglishCount(message) * 100 >= wordPercentage

