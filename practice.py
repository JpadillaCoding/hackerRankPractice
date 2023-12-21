def lonelyinteger(a):
    # Write your code here
    myList = []
    argLen = len(a)
    for x in range(argLen):
        if a[x] not in myList:
            myList.append(a[x])
        else:
            myList.remove(a[x])
    return myList[0]