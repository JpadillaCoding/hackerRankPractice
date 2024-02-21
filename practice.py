def findClosestElements(arr, k, x):
    # regular binary search to find closest to x or exact
    # return index with closest or exact to x 
    # now search to items next to it?
    # make left and right pointers 
    # answer needs to be sorted


    def binarySearch(arr,target):

        left = 0 
        right = len(arr) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid 
            if target <= arr[mid]:
                right = mid - 1

            else:
                left = mid + 1
        
        return mid 
    
    closest = binarySearch(arr, x)
    print(closest)
    # make a loop to remvoe from the counter k
    # make 2 pointers left adn right to navigate both sides of the closest
    # whiever is less left or right with min() then push onto array
    # use method depending if it's added with left or right
    left = closest
    right = closest
    while k > 1:

        if (abs(x - arr[left - 1]) <= abs(arr[right + 1] - x) ) and left > 0 :
            left = left - 1
        else:
            right = right + 1
        k = k - 1
    print(arr[left:right + 1])


findClosestElements([-2,-1,1,2,3,4,5],7,3)