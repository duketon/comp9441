# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

from challenge_3 import crack_single_byte_XOR

def detect_single_XOR():
    """Returns the string in a file that has been encrypted using single byte XOR
    >>> detect_single_XOR()
    ('7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f\\n', 80.23, b'Now that the party is jumping\\n')
    """
    candidates = list()
    with open("resources/4.txt", "r") as file_handle:
        for line in file_handle:
            result = crack_single_byte_XOR(line.strip())
            candidates.append((line, result[1], result[2]))

    return max(candidates, key=lambda item:item[1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
