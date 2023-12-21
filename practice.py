def countingSort(arr):
    # Write your code here
    arrayLength = len(arr)
    sortArray = [0] * 100
    for i in range(arrayLength):
        sortArray[arr[i]] += 1
    return sortArray