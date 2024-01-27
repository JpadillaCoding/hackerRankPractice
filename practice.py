def sortColors(nums):
    zero = 0
    one = 0
    two = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zero += 1
        if nums[i] == 1:
            one += 1
        if nums[i] == 2:
            two += 1
    for i in range(len(nums)):
        if zero > 0:
            nums[i] = 0
            zero -= 1
        elif one > 0:
            nums[i] = 1
            one -= 1
        else:
            nums[i] = 2
            two -= 1
    print(nums)
sortColors([2,0,2,1,1,0])