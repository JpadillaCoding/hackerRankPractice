def sortedSquares(nums):
# first make the ability to square. 
# need to figure out a way to sort in place instead of after
    # possibility of removing the negative signs from each since tht doesn't matter
    # could also start as the first positive number and have two pointers, one going forward and then going backwards
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    print(nums)
sortedSquares([-4,-1,0,3,10])
