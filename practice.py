def findMaxAverage(nums, k):
    # sliding window with length of k
    # return the highest average number
    windowSum = maxSum = sum(nums[:k])

    for i in range(k, len(nums)):
        windowSum += nums[k] - nums[i-k]

        maxSum = max(maxSum, windowSum)
    print(maxSum/k)
findMaxAverage([1,12,-5,-6,50,3], 4)



















"""     arrayLength = len(nums)
    if arrayLength < k:
        print(0)
    for i in range(arrayLength):
        subArr = nums[i:i+k]
        if len(subArr) == 4: print(subArr) """