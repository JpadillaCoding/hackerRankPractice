def findMaxAverage(nums, k):
    # sliding window with length of k
    # return the highest average number
    arrayLength = len(nums)
    largest_sum = sum(nums[:k])

    for i in range(1,arrayLength - k + 1):
        if sum(nums[i:i+k]) > largest_sum:
            largest_sum = sum(nums[i:i+k])
    print(largest_sum / k)

findMaxAverage([], 14538)



















"""     arrayLength = len(nums)
    if arrayLength < k:
        print(0)
    for i in range(arrayLength):
        subArr = nums[i:i+k]
        if len(subArr) == 4: print(subArr) """