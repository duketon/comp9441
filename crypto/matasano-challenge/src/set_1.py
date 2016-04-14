# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

# Challenge 1
# Convert hex to base64

import base64
import binascii

def hex_to_base64(hex_str):
    """Convert the hexademical input into base64
    >>> hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    """
    binary = binascii.unhexlify(hex_str)
    return base64.b64encode(binary)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
