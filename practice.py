def peakIndexInMountainArray(arr):
    # find the peak index in mountain array
    # Could brute force to go through and find largest number
    # could use binary search to find an index where the
    # left and right numbers are smaller
    left = 0 
    right = len(arr) - 1
    while left <= right: 

        mid = left + (right - left) // 2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
            print (mid)
            break
        elif arr[mid] < arr[mid - 1]:
            right = mid 
        else:
            left = mid 

peakIndexInMountainArray([3,9,8,6,4])