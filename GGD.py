__author__ = 'Geoffrey'

def getGGD(first, second):
    dividend = 0
    divisor = 0

    if first > second:
        dividend = first
        divisor = second
    else:
        dividend = second
        divisor = first

    quotient = int(dividend / divisor)
    remainder = dividend - (quotient * divisor)

    while remainder:
        dividend = divisor
        divisor = remainder
        quotient = int(dividend / divisor)
        remainder = dividend - (quotient * divisor)

    print "Greatest Common Divisor: ", divisor
    return divisor


