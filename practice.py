def searchMatrix(matrix, target):
    # make a function with a standard binary search for the ineer search
    # make a binary search that checks the last digit of each sub

    left = 0 
    right = len(matrix) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if matrix[mid][0] <= target and matrix[mid][-1] >= target:
            innerLeft = 0
            innerRight = len(matrix[mid]) - 1

            while innerLeft <= innerRight:
                
                innerMid = innerLeft + (innerRight - innerLeft) // 2
                
                if matrix[mid][innerMid] == target:
                    print(True)
                if matrix[mid][innerMid] > target:
                    innerRight = innerMid - 1
                else:
                    innerLeft = innerMid + 1
            print(False)

        if matrix[mid][-1] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(False)
searchMatrix([[1,3,5]], 1)