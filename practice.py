def getRow(rowIndex: int):
    #considering it can be 0 
    triangle = [[1]]
    if rowIndex == 0:
        return triangle[0]
    for i in range(0,rowIndex):
        # outer loop to keep track of the prev row, the last row
        # since we're adding on top each iteration
        prevRow = triangle[-1]
        curRow = [1] # start with 1 since triangle always does
        for j in range(1,len(prevRow)):
            curRow.append(prevRow[j-1] + prevRow[j])
        curRow.append(1)
        triangle.append(curRow)
    print(triangle[rowIndex])
getRow(3)