# Crypto Challenge Set 1 - The Basics
# http://cryptopals.com/sets/1/

from challenge_3 import xor_single_char

def repeating_key_XOR(plain_text, keys):
    """Performs a repeating XOR encryption. Given a set of cipher keys [K1, K2, .., Kn], perform XOR for each byte of the
    plain text with K1, K2, .., Kn, K1, K2, ..., Kn.
    >>> repeating_key_XOR("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", "ICE")
    '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    """
    result = ''
    int_keys = [ord(letter) for letter in keys]
    i = 0
    for letter in plain_text:
        result += chr(ord(letter) ^ int_keys[i])
        i  = (i + 1) % len(int_keys)
    return result.encode('hex')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

