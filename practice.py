def divisorGame(n):
    # the number chosen has to be more than 0 and less than n 
    # number chosen has to be modulus 0
    # start loop from current n count down for most optimal
    # alice goes first- figure out how to know if alice wins
    # return true if alice wins

    #init the current number the game is one 
    currentNum = n
    #set a counter to count down and find the highest possible modulus 0
    counter = currentNum - 1
    aliceTurn = True
    while counter > 0:
        # if found then remove from the current num
        if (counter % n == 0) and counter > 0:
            currentNum = currentNum - counter
        else: 
            #someone won
            if aliceTurn == True:
                print(False)
            else:
                print(True)
        counter = counter - 1
divisorGame(2)
