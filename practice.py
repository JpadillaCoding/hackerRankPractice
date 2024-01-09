def threeSum(nums):
    # find instances in the array where all three added up = 0 
    # itirate through each number
    # for each itieration the remainign tow use two pointer system 
    # use comparison of adding the remainders together is more than 0, reduce right
    # if less than 0, increase left
    # check if the set is already made
    nums.sort()
    triplets = []
    for i in range(len(nums) - 1):
        if nums[i] == 0: print(triplets)
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                if [nums[i], nums[left], nums[right]] not in triplets:
                    triplets.append([nums[i], nums[left], nums[right]])
                left += 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else: 
                right -= 1
    print(triplets)

    # return the triplets as their values in arrays. multiple are possible
threeSum([0,0,0])