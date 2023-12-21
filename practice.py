def birthday(s, d, m):
    counter = 0
    arrLen = len(s)
    if arrLen < m:
        return 0
    for i in range(arrLen):
        subArray = (s[i:i+m])
        if len(subArray) == m:
            if sum(subArray) == d:
                counter += 1
    return (counter)


birthday([2,2,1,3,2], 4, 2)