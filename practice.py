def divisorSubstrings(num,k):

    # make string into array 
    stringNum = str(num)
    splitNum = []
    count = 0
    for i in range(len(stringNum)): splitNum.append(stringNum[i])
    # use k to get the "window" needed to 
    for i in range(0,len(splitNum)-k+1):
        currentNum = splitNum[slice(i,i+k)]
        joinedNum = int(''.join(currentNum))
        if joinedNum != 0 :
            if num % joinedNum == 0:
                count += 1
    print(count)
divisorSubstrings(240, 2)