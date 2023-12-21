def birthday(s, d, m):
    # loop through S to find sums of D with the length of M
    # outer loop to go through full array
    counter = 0
    arrLen = len(s)
    # edge case of length of array is greater than M
    for i in range(arrLen):
        # inner loop only iterates the length of M  
        print(s[i:i+m])
            # check if the sum of those are equal to D 
                # if so add to counter
                # edge case of making single it is a length of m 
    # return counter 


birthday([2,2,1,3,2], 4, 2)