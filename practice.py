def twoSum(numbers,target):
    # have a left pointer at 0 and a right pointer at last num
    # if left + right == target return indices + 1 on each
    # if target is less, decrease right pointer 
    # if target is more than, increase left pointer


    left = 0 
    right = len(numbers) -1 

    while left < right:

        if numbers[left] + numbers[right] == target:
            print ([left+1,right+1])
            break
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

twoSum([-1,0], -1)