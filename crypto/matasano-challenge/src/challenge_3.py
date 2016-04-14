# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

import math

char_frequencies = {
    'a':  8.167,
    'b':  1.492,
    'c':  2.782,
    'd':  4.253,
    'e':  12.702,
    'f':  2.228,
    'g':  2.015,
    'h':  6.094,
    'i':  6.966,
    'j':  0.153,
    'k':  0.772,
    'l':  4.025,
    'm':  2.406,
    'n':  6.749,
    'o':  7.507,
    'p':  1.929,
    'q':  0.095,
    'r':  5.987,
    's':  6.327,
    't':  9.056,
    'u':  2.758,
    'v':  0.978,
    'w':  2.361,
    'x':  0.150,
    'y':  1.974,
    'z':  0.074,
    ' ':  8,
}

def score(str_bytes):
    """Sums the character frequency for each character. If the given byte cannot be mapped to a character then it gets a score of 0."""
    freq_score = sum([char_frequencies.get(chr(letter).lower(), -100) for letter in str_bytes])
    return math.ceil(freq_score * 100) / 100


def xor_single_char(str_bytes, key):
    """Performs an XOR between a byte array and an integer"""
    output = b''

    for char in str_bytes:
        output += bytes([char ^ key])

    return output


def crack_single_byte_XOR(cipher_text):
    """Attempts to crack a single byte XOR through character frequency analysis. Returns a tuple containing the key, score, and deciphered plain_text
    >>> crack_single_byte_XOR("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    (88, 86.08, b"Cooking MC's like a pound of bacon")
    """
    candidates = list()
    cipher_bytes = bytes.fromhex(cipher_text)

    for key_candidate in range(256):
        byte_candidate = xor_single_char(cipher_bytes, key_candidate)
        candidates.append((key_candidate, score(byte_candidate), byte_candidate))

    return max(candidates, key=lambda item: item[1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
