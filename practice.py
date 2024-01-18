def threeSumClosest(nums,target):
# sort the array,
# use for loop to go through each number
    # if target is currentSum < target: start += 1
    nums.sort()
    diff = float('inf')
    answer = float('inf')

    for i in range(len(nums)-1):
        start = i + 1
        end = len(nums) - 1

        while start < end:
            currentSum = nums[i] + nums[start] + nums[end]
            if currentSum == target:
                return target
            elif abs(currentSum - target) < diff:
                diff = abs(currentSum - target)
                answer = currentSum
            if target < currentSum:
                end -= 1
            else:
                start += 1
    return(answer)

threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2)