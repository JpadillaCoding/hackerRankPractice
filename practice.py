def canPlaceFlowers(flowerbed, n: int):
    counter = 0
    if n == 0: 
        print(True)
    for plot in range(len(flowerbed)):
        if flowerbed[plot] == 0 and (plot == 0 or flowerbed[plot - 1] == 0) and (plot == len(flowerbed)-1 or flowerbed[plot + 1] == 0):
            flowerbed[plot] = 1
            counter += 1 
            if counter == n: print(True) 
    print(False)
canPlaceFlowers([0,0,0,0,1], 2)