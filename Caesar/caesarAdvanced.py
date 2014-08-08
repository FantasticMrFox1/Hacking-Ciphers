# Caesar Cipher Advanced
# The second example of Hacking Secret Ciphers
# This shifts all 126 printable ASCII characters.
# Raymond Ho

message = raw_input("Enter your message: ")
mode = raw_input("E for Encrypt, D for Decrypt: ")
key = int(raw_input("Enter your key: "))
offset = 31 # For Encryption

# Key must be 0 - 32
if key > 32: key = key % 32

newString = ''
if mode == 'D' or mode == 'decrypt':
    key = -key
    offset = 95 # for Decryption

for c in message:
    num = (ord(c) + key) % 126
    if num < 32:
        num += offset
    newString += chr(num)
print newString

