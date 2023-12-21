def diagonalDifference(arr):
    # Write your code here
    arrLength = len(arr)
    positiveTotal = 0
    negativeTotal = 0
    for i in range(arrLength):
        positiveTotal = positiveTotal + arr[i][i]
    for i in range(arrLength):
        negativeTotal = negativeTotal + arr[i][arrLength-i-1]
    return abs(positiveTotal - negativeTotal)