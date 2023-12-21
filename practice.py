def flippingBits(n):
    bitFormat = list('{:032b}'.format(n))
    bitFormatLen = len(bitFormat)
# loop through each bit and flip
    for bit in range(bitFormatLen):
        if bitFormat[bit] == '0':
            bitFormat[bit] = '1'
        elif bitFormat[bit] == '1':
            bitFormat[bit] = '0'
# covert back to int
    bitFormat = ''.join(bitFormat)
    n = int(bitFormat,2)
# return opposite of bit formate fort each one
    return(n)

flippingBits(2147483647) 