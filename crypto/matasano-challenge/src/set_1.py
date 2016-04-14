# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

import base64
import binascii

# Challenge 1
# Convert hex to base64
def hex_to_base64(hex_str):
    """Convert the hexademical input into base64
    >>> hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    """
    binary = binascii.unhexlify(hex_str)
    return base64.b64encode(binary)


# Challenge 2
# Fixed XOR on two hex buffers
def fixed_XOR(hex_a, hex_b):
    """XOR two hexadecimal buffers of equal length
    >>> fixed_XOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    '746865206b696420646f6e277420706c6179'
    """
    xored = int(hex_a, 16) ^ int(hex_b, 16)
    return '{:x}'.format(xored)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
