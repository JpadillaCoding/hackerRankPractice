def canThreePartsEqualSum(arr):
    # conditions that need to be met:
    # sum must be modulo 3 
    # only way to divide by 3 is every sum being the same
    # find the amount the array neesd rto be dvided by (avg)
    # do while 
    # move left pointer until the avg number is found
    # move the right pointer until the avg num is found backwards
    # check if left middle and right are equal
    total = sum(arr)
    if total % 3 != 0:
        print(False)
    avg = total // 3 
    left = 1
    leftFlipped = False
    right = len(arr) - 1
    rightFlipped = False
    while left < right:
        leftsum = sum(arr[:left])
        rightsum = sum(arr[right:])
        if leftsum != avg:
            left += 1
        else:
            leftFlipped = True
        if rightsum != avg:
            right -= 1
        else:
            rightFlipped = True
        if leftFlipped and rightFlipped and sum(arr[left:right]) == avg:
            print(True)
        elif leftFlipped and rightFlipped:
            print(False)
            break
    print(False)
canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])