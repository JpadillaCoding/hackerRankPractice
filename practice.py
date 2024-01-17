def threeSumClosest(nums,target):
# do a for loop to through each iteration 
    # a while loop to use tow pointers to check everything inbetween
    # a min variable that keeps track of closest amount
        # find closest amount with min(all 3 - target, currrent min)
            # use absolute after the different is found to negate negatives
    closest = abs((nums[0] + nums[1] + nums[-1]) - target)
    sumTotal = nums[0] + nums[1] + nums[-1]

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if abs((nums[i] + nums[left] + nums[right]) - target) < closest:
                closest = abs((nums[i] + nums[left] + nums[right]) - target)
                sumTotal = nums[i] + nums[left] + nums[right]
            if target < closest:
                right -= 1
            else:
                left += 1
    print(sumTotal)
threeSumClosest([1,1,1,0],100)