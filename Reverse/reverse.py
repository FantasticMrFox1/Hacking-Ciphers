# Reverse Cipher
# The first example of Hacking Secret Ciphers
# A simple, weak cipher to encrypt a string.
# Raymond Ho

message = raw_input("Enter your string: ")

# Look at this pythonic way..
print message[::-1]

# The uglier way
translated = ''
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i -= 1

print(translated)


