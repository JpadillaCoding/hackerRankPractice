def miniMaxSum(arr):
    # Write your code here
    arrLength = len(arr)
    arr.sort()
    minTotal = sum(arr[0:arrLength-1])
    maxTotal = sum(arr[1:arrLength])
    print(minTotal, maxTotal)
