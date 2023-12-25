def countingbits(num):

    # make a loop since of n 
    # for n get the bit representition
    # add up all ones with sum of string
    # append to results array

    resultsArray =[]
    for i in range(num+1):
        currentNum = '{0:b}'.format(i)
        bitArray = []
        for char in currentNum:
            bitArray.append(int(char))
        resultsArray.append(sum(bitArray))
        return(resultsArray)

countingbits(5)