def minimumDifference(nums,k):

    # do i need to sort? 
    # sort the array
    # make a variable to track the current lowest diff
    # loop through all and comparing differences between [0]and[-1]
    # sliding window for comparison 
    # use k to get the window
    # return lowest diff variable

    nums.sort()
    lowestDelta = 0
    if len(nums) == 1 :
        lowestDelta = 0
    elif len(nums) == k:
        lowestDelta = nums[-1] - nums[0]
    else:
        lowestDelta = nums[k] - nums[0]
    for i in range(len(nums)-k+1):
        windowDelta = nums[i:i+k]
        highest = windowDelta[-1]
        lowest = windowDelta[0]
        delta = highest - lowest

        if (lowestDelta > delta):
            lowestDelta = delta
    print(lowestDelta)
minimumDifference([4407,3036], 2)