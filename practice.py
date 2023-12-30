def minSubsequence(nums):
    # given an array find which set of numbers returns a greater value than rest
    # set the total sum
    # sort reverse to count highest digits first
    # loop through and compare the count with the total sum
        # if greater return the subarray
    total = sum(nums)
    subTotal = 0
    nums.sort(reverse = True)
    for digit in range(len(nums)):
        subTotal += nums[digit]
        total -= nums[digit]
        if subTotal > total:
            print(nums[:digit+1])
    print(nums)

minSubsequence([4,4,7,6,7])