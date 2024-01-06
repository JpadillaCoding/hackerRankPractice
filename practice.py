def generate(numRows: int):
    # make the initial triangle since always starts with 1 
    # 2 loops. one for the subarray
    # keep track of the previous array
    # start the new row with 1 always and append 1 at end always

    triangle = [[1]]
    for i in range(1,numRows):
        prev_row = triangle[-1] # access last item 
        new_row = [1] # start with 1 since they all do

        for j in range(1,len(prev_row)):
            new_row.append(prev_row[j-1] + prev_row[j])
            print(prev_row)
        new_row.append(1)
        triangle.append(new_row)
        print(triangle)

generate(5)