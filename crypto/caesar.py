# Caesar Encryption, Decryption and Brute Force cracking

import string

# Performs ROTN on the inputted message, where N = key.
def rot_n(message, key):
    chars = string.ascii_lowercase
    scheme = string.maketrans(chars, chars[key:] + chars[:key])
    return message.translate(scheme)

# Encrypts message using key with the Caesar Cipher
def encrypt(message, key):
   encrypted = rot_n(message, key)
   return "".join(encrypted)

# Decyprts message using key with the Caesar Cipher
def decrypt(message, key):
    decrypted = rot_n(message, -key)
    return "".join(decrypted)

# Brute Force crack over a Caesar Cipher encrypted message. Prints to stdout.
# Since there are only 26 possible results, manual inspection is fine to determine the
# correctly deciphered plain text.
def crack(message):
    for key_candidate in range(0,26):
        attempt = decrypt(message, key_candidate)
        print("Candiate key : {} produces {}".format(key_candidate, attempt))
