def search(nums,target):
    # binary search 
    left = 0 
    right = len(nums) - 1
    flipped = False
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return(mid)
        if nums[mid] > nums[left]:
            left = mid 
        else: 
            right = mid

    return(-1)
search([4,5,6,7,0,1,2],0)