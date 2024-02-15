def search(nums,target):
    # binary search
    # need to check if our mid is in left or right sorted array
    # if on right, check if mid is less than left to check after pivot
    # or chekc if greater than mid to look to right of mid
    # else its on the left
    # vice versa for right

    left = 0 
    right = len(nums) - 1 

    while left <= right:

        mid = left + (right-left) // 2
        if nums[mid] == target:
            print(True)
            return True
        if nums[mid] >= nums[left]:
            
            if target < nums[left]:
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else: 
                right = mid - 1
        else:
            if target > nums[right]:
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    print(False)
    return False
search([1,0,1,1,1],0)