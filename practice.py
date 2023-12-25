def arrayPairSum(arr):
    # Get the maximum number that can be made with all minumum pairs 
    # easiest way to do this sort all
    # check to make sort works here unlike js
    # return the same of all pairs
    # can increase time by adding algo to sort 
    arr.sort()
    total = 0
    for i in range(0,len(arr),2):
        total += arr[i]
    print(total)
arrayPairSum([6,2,6,5,1,2])
# [6,2,6,5,1,2]
    

