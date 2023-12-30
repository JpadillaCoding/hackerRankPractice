def canThreePartsEqualSum(arr):
    # left pointer start at 0 
    # right pointer start at -2 
    # check if 0- left pointer = right pointer total
        # check if [0-left] = [left - right] = [right - -1]
    # move left + 1 
    # move right - 1
    left = 0 
    right = len(arr) - 2
    if len(arr) < 3: 
        print(False) 

    while left < right:
        if sum(arr[:left]) == sum(arr[left+1:right]) == sum(arr[right:-1]):
            print(True, sum(arr[:left]), sum(arr[left:right]), sum(arr[right:-1]))
        else:
            left += 1
            right -= 1
    print(False)

# edge cases:
    # length < 3 == false
    # length == 3 check [0] == [1] == [2]
canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])