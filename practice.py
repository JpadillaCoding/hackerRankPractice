def largestPerimeter(nums):
    # addition of any 2 sides is grreater than 3rd side
    # start with 3 biggest numbers
    # sort(reverse = true)
    # loop through
    nums.sort(reverse=True) 
    for a in range(len(nums)-2):
        if (nums[a] + nums[a+1] > nums[a+2]) and (nums[a] + nums[a+2] > nums[a+1]) and (nums[a+1] + nums[a+2] > nums[a]):
            print(nums[a]+nums[a+1]+nums[a+2])
    print(0)
    


largestPerimeter([2,1,2])
    