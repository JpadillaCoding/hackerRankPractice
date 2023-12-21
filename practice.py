def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positives = 0
    negatives = 0
    zeros = 0
    for i in range(n):
        if (arr[i] > 0):
            positives += 1
        elif (arr[i] == 0):
            zeros += 1
        else:
            negatives += 1
            
    positiveRatio = positives / n
    negativeRatio = negatives / n
    zeroRatio = zeros / n

    print(f"{positiveRatio:.6f}")
    print(f"{negativeRatio:.6f}")
    print(f"{zeroRatio:.6f}")