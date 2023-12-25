def minimumRecolors(blocks,k):
    #check if k is in block by multiplying the k by b 
    # if not then loop 
    # make a window of 7 looking for the container with the most amount of black
    # loop in window to count b
    # return the difference between highest and  k 
    quickCheckSet = ''.join(['B']*k)
    highestBlack = 0
    if quickCheckSet in blocks:
        print(0)
    else: 
        for i in range(len(blocks)-k+1):
            window = blocks[i: i+k]
            totalBlacks = 0
            for char in range(len(window)):
                if window[char] == 'B': totalBlacks += 1
            if totalBlacks > highestBlack: highestBlack = totalBlacks

    print(k-highestBlack)
minimumRecolors("WBWBBBW",2)