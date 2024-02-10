def findPeakElement(nums):
    # binary search 
    # find spot where left and right of mid are less
    # or left same as mid and right less
    # or right same as mid and left less

    left = 0 
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]) or (nums[mid] == nums[mid - 1] and nums[mid] > nums[mid + 1]) or (nums[mid] > nums[mid - 1] and nums[mid] == nums[mid + 1]):
            #only first conditional is actually needed
            # at first I thought I would need to check for same adjacent nums
            # but question says this is not possible
            print(mid)
            break
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid - 1
    print(left)
findPeakElement([1,2,3,4])