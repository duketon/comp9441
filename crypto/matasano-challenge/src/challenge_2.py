# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

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
