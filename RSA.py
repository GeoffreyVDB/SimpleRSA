__author__ = 'Geoffrey'

import math

cipher = "0011000100011010101010101001001000" \
         "0110111101101111101010001111110001" \
         "0011110110101101101111011101000011" \
         "0101010110011100000111000001111101"

n = 69647
e = 53

def generatePrimes(n):
    sqrtN = int(math.floor(math.sqrt(n)))
    while 1:
        result = n % sqrtN
        if result == 0:
            break
        else:
            sqrtN -= 2
    p = sqrtN
    q = n / p
    return p, q

def inverse(a, m):
  for x in range (0, m):
    if (((a * x) % m) == 1 ):
        return x
  return 0

def decrypt(cipher):
    split_cipher = [cipher[i:i+17] for i in range(0, len(cipher), 17)]
    decrypted = ""
    for item in split_cipher:
        bits = (bin(pow(int(item, 2), d, n))[2:].zfill(16))
        first = bits[:len(bits)/2]
        second = bits[len(bits)/2:]
        decrypted += chr(int(first, 2)) + chr(int(second, 2))
    return decrypted

p, q = generatePrimes(n)
d = inverse(e, ((p-1)*(q-1)))
print decrypt(cipher)

print "p: ", p
print "q: ", q
print "d: ", d