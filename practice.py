def findMaxAverage(nums, k):
    # sliding window with length of k
    # return the highest average number
    arrayLength = len(nums)
    for i in range(arrayLength):
        subarray = nums[i:i+k]
        if len(subarray) == 4: print(nums[i:i+k])

findMaxAverage([1,12,-5,-6,50,3], 4)



















"""     arrayLength = len(nums)
    if arrayLength < k:
        print(0)
    for i in range(arrayLength):
        subArr = nums[i:i+k]
        if len(subArr) == 4: print(subArr) """