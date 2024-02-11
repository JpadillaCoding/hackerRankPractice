def search(nums,target):
    # binary search 
    left = 0 
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            print(mid)

        # mid is in the left section, we have to switch to right
        if nums[left] <= nums[mid]:
            # check if 
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[right]:
                right = mid - 1
            else: 
                left = mid + 1
    return -1
search([4,5,6,7,0,1,2],0)