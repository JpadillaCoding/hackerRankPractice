def findWinner(s):
    problemString = list(s)
    global Alice
    Alice = True
    global gameComplete
    gameComplete = False


    def playerTurn():
        global gameComplete
        global Alice
        print("Turn: " ,Alice)
        flipsMade = False
        playerLetter = ''
        if Alice == True:
            playerLetter = 'w'
        else:
            playerLetter = 'b'
        for i in range(1, len(problemString) - 1):
            if problemString[i] == playerLetter and problemString[i+1] == playerLetter and problemString[i-1] == playerLetter:
                del problemString[i]
                Alice = not Alice
                flipsMade = True
                break
        if flipsMade == False:
            gameComplete = True
    
    while gameComplete == False:
        playerTurn()


    print("Final: " ,Alice)

findWinner('wwwbbbbwww')



""" def gameWinner(colors):
    problemString = list(colors)  # Convert string to list for easy modification
    i = 1  # Start from the second character
    wendyTurn = True
    def game(player, problemString):
        while i < len(problemString) - 1:
            if problemString[i-1] == 'w' and problemString[i] == 'w' and problemString[i+1] == 'w':
                # Remove 'w' at the current index
                problemString.pop(i)
                wendyTurn = not wendyTurn
                break
            else:
                i += 1  # Move to the next character

        result = ''.join(problemString)
        print(result)
gameWinner('wwwbbbbwww') """


""" def subarraySum(arr):
    arrLen = len(arr)
    result = 0
    for start in range(arrLen):
        for j in range(start, arrLen):
            subArraySum = 0
            for k in range(i, j+ 1):
                subArraySum += arr[k]
            result += subArraySum
    return result
subarraySum([4,5,6]) """
    

