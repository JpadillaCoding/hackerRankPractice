def findPeakElement(nums):
    # binary search 
    # find spot where left and right of mid are less
    # or left same as mid and right less
    # or right same as mid and left less

    left = 0 
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) //2

        if (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]) or (nums[mid] == nums[mid - 1] and nums[mid] > nums[mid + 1]) or (nums[mid] > nums[mid - 1] and nums[mid] == nums[mid + 1]):
            print(mid)
            break
        if nums[mid] < nums[mid+1]:
            left = mid
        else:
            right = mid
findPeakElement([1,2,3,1])