def numSubarrayProductLessThanK(nums, k):
    # need to check for all sub arrays that the product is less than k
    # for loop start at 0
    # while loop end and goes backwards
    end = len(nums) - 1
    count = 0
    for i in range(len(nums)):
        # forward exploration 
        explorer = i
        currentProd = nums[i]
        if currentProd < k:
            count += 1
        while explorer < end:
            explorer += 1
            currentProd = currentProd * nums[explorer]
            # optimzation of if it is product => k:
                # get out of while loop
            if currentProd < k:
                count += 1
    print(count)
numSubarrayProductLessThanK([10,5,2,6], 100)
"""     
    10 5 2 6
    10 5 2
    10 5
    10
    5 2 6
    5 2
    5
    2 6
    2
    6 """