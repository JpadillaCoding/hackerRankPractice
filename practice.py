def minimumTotal(triangle):
    # tier below has a window of only i + 1 and i - 1 
    # find min in that window
    # make new window
    # keep adding as we go
    total = triangle[0][0]

    for i in range(1,len(triangle)):
        lPointer = max(0,i-1)
        rPointer = min(len(triangle[i]), i+1)
        # where to track the min inside the subarray? 
        minFound=triangle[i][lPointer]
        for j in range(lPointer, rPointer):
            minFound = min(minFound, triangle[i][j])
        total += minFound
    print(total)
    
minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])