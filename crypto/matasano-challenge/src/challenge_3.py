# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

# Simple ranking of most commonly occuring characters
char_frequencies = {
    'e': 27,
    't': 26,
    'a': 25,
    'o': 24,
    'i': 23,
    'n': 22,
    's': 21,
    'r': 20,
    'h': 19,
    'l': 18,
    'd': 17,
    'c': 16,
    'u': 15,
    'm': 14,
    'f': 13,
    'p': 12,
    'g': 11,
    'w': 10,
    'y': 9,
    'b': 8,
    'v': 7,
    'k': 6,
    'x': 5,
    ' ': 4,
    'j': 3,
    'q': 2,
    'z': 1
}

def score(str_bytes):
    """Sums the character frequency for each character. If the given byte cannot be mapped to a character then it gets a score of 0."""
    return sum([char_frequencies.get(chr(letter).upper(), 0) for letter in str_bytes])


def xor_single_char(str_bytes, key):
    """Performs an XOR between a byte array and an integer"""
    output = b''

    for char in str_bytes:
        output += bytes([char ^ key])

    return output


def crack_single_byte_XOR(cipher_text):
    """Attempts to crack a single byte XOR through character frequency analysis.
    >>> crack_single_byte_XOR("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    "Cooking MC's like a pound of bacon"
    """
    candidates = list()
    cipher_bytes = bytes.fromhex(cipher_text)

    for key_candidate in range(256):
        byte_candidate = xor_single_char(cipher_bytes, key_candidate)
        candidates.append((key_candidate, score(byte_candidate), byte_candidate))

    return max(candidates, key=lambda item: item[1])[2].decode("ascii")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
