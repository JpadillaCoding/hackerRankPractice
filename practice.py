def largestSumAfterKNegations(nums, k):
    # sort the numbers
    # sub the lowest num with a - 
    # flip any negative numbers 
        # now continue to flip the smallest number k times
    nums.sort()
    counter = k
    smallest = nums[-1]
    for i in range(len(nums)):
        if counter > 0 and nums[i] < 0:
            # compare new value with smallest and repalce
            nums[i] = -nums[i]
            counter -= 1
            if smallest > nums[i]:
                smallest = i
        else : break
    nums.sort()
    while counter > 0:
        nums[0] = -nums[0]
        counter -= 1
    print(sum(nums))
    # keep flipping smallest


largestSumAfterKNegations([3,-1,0,2],3)