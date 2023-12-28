def canPlaceFlowers(flowerbed, n: int):
    # single loop that checks if i+1 and i-1 and i are 0's 
    # add to counter
    # if counter == n then print true
    counter = 0
    if len(flowerbed) > 2:
        for plot in range(0,len(flowerbed)-1):
            if plot == 0:
                if flowerbed[plot] == 0 and flowerbed[plot + 1] == 0:
                    counter += 1
                    flowerbed[plot] = 1
            if flowerbed[plot] == 0 and flowerbed[plot - 1] == 0 and flowerbed[plot + 1] == 0:
                counter += 1
                flowerbed[plot] = 1
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            counter += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            counter += 1
    elif len(flowerbed) == 2: 
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            counter += 1
    else:
        if flowerbed[0] == 0:
            counter += 1
    if counter >= n:
        print(True)
    print(False)

    # edge case of index 0 and -1 having 0 with -2 and 1 having 0 then + 1 
    # check last 
canPlaceFlowers([0,0,0,0,1], 2)