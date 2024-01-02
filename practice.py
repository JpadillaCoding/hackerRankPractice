from typing import List
def maxArea(height):
    # find the max area of between two indeces 
    # width = rightPoint - LeftPoint
    # the height will always be the lower of the 2 
    # have left and right pointer that move on case:
        # whichever side has the smaller of 2 heights, move by 1 
        # keep track of max

    maxFound = 0
    right = len(height) - 1
    left = 0 

    while left < right:
        if height[left] > height[right]:
            maxFound = max(maxFound,height[right] * (right - left))
            right -= 1 
        else:
            maxFound = max(maxFound,height[left] * (right - left))
            left += 1

    print(maxFound)
    

maxArea([1,1])