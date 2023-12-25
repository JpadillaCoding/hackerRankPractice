def maxSumTwoNoOverlap(nums, firstLen, secondLen):
    # use one window to go through and find max
    # when max is found make array with index points
    # use second window to go through and find max. 
    # if max is greater than current max also needs to not be in index.
    firstLenMax = 0
    firstLenIndeces = []
    secondLenMax = 0
    for i in range(len(nums)-firstLen+1):
        windowMax = sum(nums[i: i+firstLen])
        if windowMax > firstLenMax:
            firstLenMax = windowMax
            firstLenIndeces = []
            for j in range(i, i+firstLen):
                firstLenIndeces.append(j)
            print(firstLenIndeces)

    for i in range(len(nums)-secondLen+1):
        windowMax = sum(nums[i:i+secondLen])
        if windowMax > firstLenMax:
            
maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3,2)