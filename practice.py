def sortedSquares(nums):
# first make the ability to square. 
# need to figure out a way to sort in place instead of after
    # possibility of removing the negative signs from each since tht doesn't matter
    # maybe have an if statement if it is below 0 put into new list with insert at 0 
    # make new list to return
        # in this list start with left pointer at start and right pointer at end.
            # sort as i go
    # what if when we find the one that is greater than that's the only one that moves
    squares = []
    left = 0
    right = len(nums) - 1
    while left <= right:
        leftSquare = nums[left] * nums[left]
        rightSquare = nums[right] * nums[right]

        if leftSquare > rightSquare:
            squares.insert(0,leftSquare)
            left += 1 
        else:
            squares.insert(0,rightSquare)
            right -=1
    print(squares) 
sortedSquares([-4,-1,0,3,10])
